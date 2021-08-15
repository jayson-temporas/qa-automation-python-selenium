<?php

namespace Tests\Unit;

use App\User;
use App\Task;
use Illuminate\Database\Eloquent\Collection;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class UserTest extends TestCase
{
    use RefreshDatabase;
    
    /** @test */
    public function a_user_has_tasks()
    {
        $user = factory('App\User')->create();

        $this->assertInstanceOf(Collection::class, $user->tasks);
    }
}
