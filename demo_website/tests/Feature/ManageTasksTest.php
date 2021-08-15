<?php

namespace Tests\Feature;

use App\Task;
use App\User;
use App\Jobs\SendTaskCreatedEmail;
use App\Mail\TaskCreatedEmailNotification;
use Illuminate\Support\Facades\Mail;
use Illuminate\Support\Facades\Queue;
use Illuminate\Events\CallQueuedListener;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ManageTasksTest extends TestCase
{
    use RefreshDatabase;
    
    /** @test */
    public function guests_cannot_manage_tasks()
    {
        $task = factory(Task::class)->create();

        $this->get(route('tasks.index'))->assertRedirect('login');
        $this->get(route('tasks.create'))->assertRedirect('login');
        $this->get(route('tasks.edit', $task->id))->assertRedirect('login');
        $this->post(route('tasks.store'), factory(Task::class)->raw())->assertRedirect('login');
        $this->put(route('tasks.update', $task->id), $task->toArray())->assertRedirect('login');
        $this->delete(route('tasks.destroy', $task->id))->assertRedirect('login');
    }

    /** @test */
    public function a_task_requires_a_name()
    {
        $this->signIn();

        $attributes = factory('App\Task')->raw(['name' => '']);

        $this->post(route('tasks.store'), $attributes)->assertSessionHasErrors('name');
    }

    /** @test */
    public function a_task_requires_a_description()
    {
        $this->signIn();
        
        $attributes = factory('App\Task')->raw(['description' => '']);

        $this->post(route('tasks.store'), $attributes)->assertSessionHasErrors('description');
    }

    /** @test */
    public function user_can_create_a_task()
    {
        $user = $this->signIn();

        $this->get(route('tasks.create'))->assertStatus(200);

        $this->followingRedirects()
            ->post(route('tasks.store'), $attributes = factory(Task::class)->raw(['user_id' => $user->id]))
            ->assertSee($attributes['name'])
            ->assertSee($attributes['description']);

        $this->assertDatabaseHas('tasks', $attributes);
    }

    /** @test */
    public function user_can_update_a_task()
    {
        $task = factory('App\Task')->create();

        $this->actingAs($task->user)
             ->patch(route('tasks.update', $task->id), $attributes = ['name' => 'Changed', 'description' => 'Changed'])
             ->assertRedirect(route('tasks.index'));

        $this->get(route('tasks.edit',$task->id))->assertStatus(200);

        $this->assertDatabaseHas('tasks', $attributes);
    }

    /** @test */
    public function user_can_only_see_his_own_tasks()
    {
        $user = $this->signIn();
        $userTask = factory(Task::class)->create(['user_id' => $user->id]);

        $notMe = factory(User::class)->create();
        $notMyTask = factory(Task::class)->create(['user_id' => $notMe->id]);

        $this->get(route('tasks.index'))
            ->assertSee($userTask['name'])
            ->assertSee($userTask['description'])
            ->assertDontSee($notMyTask['name'])
            ->assertDontSee($notMyTask['description']);           
    }


    /** @test */
    public function unauthorized_users_cannot_delete_tasks()
    {
        $task =  factory('App\Task')->create();

        $this->delete(route('tasks.destroy', $task->id))
            ->assertRedirect('/login');

        $user = $this->signIn();

        $this->delete(route('tasks.destroy', $task->id))->assertStatus(403);
    }

    /** @test */
    public function a_user_can_delete_a_task()
    {
        $task =  factory('App\Task')->create();

        $this->actingAs($task->user)
            ->delete(route('tasks.destroy', $task->id))
            ->assertRedirect('/tasks');

        $this->assertDatabaseMissing('tasks', $task->only('id'));
    }

    /** @test */
    public function user_must_receive_email_after_creating_a_task()
    {
        Mail::fake();
        Queue::fake();

        $user = $this->signIn();
        $task = factory('App\Task')->raw(['user_id' => $user->id]);
        $this->post(route('tasks.store'), $task);
        
        Queue::assertPushed(SendTaskCreatedEmail::class);

        $task = factory('App\Task')->create(['user_id' => $user->id]);
        
        Mail::to($user->email)->send(new TaskCreatedEmailNotification($user, $task));
        Mail::assertSent(TaskCreatedEmailNotification::class);
    }
}
