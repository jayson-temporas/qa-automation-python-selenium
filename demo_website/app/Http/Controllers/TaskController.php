<?php

namespace App\Http\Controllers;

use App\Task;
use App\Jobs\SendTaskCreatedEmail;
use \Illuminate\Http\Response;

class TaskController extends Controller
{
    public function index()
    {
        $tasks = auth()->user()->tasks()->get();

        return view('tasks.index', compact('tasks'));
    }

    public function create()
    {
        $task = new Task();
        return view('tasks.create', compact('task'));
    }

    public function store()
    {
        $task = auth()->user()->tasks()->create($this->validateRequest());

        SendTaskCreatedEmail::dispatch(auth()->user(), $task);

        return redirect()->route('tasks.index');
    }

    public function edit()
    {
        $task = Task::find(request('task'));

        return view('tasks.edit', compact('task'));
    }

    public function update(Task $task)
    {
        $task->update($this->validateRequest());

        return redirect()->route('tasks.index');
    }

    public function destroy(Task $task)
    {
        if (auth()->user()->id != $task->user->id) {
            return new Response('Forbidden', 403);
        }

        $task->delete();

        return redirect('/tasks');
    }

    protected function validateRequest()
    {
        return request()->validate([
            'name' => 'required|max:255',
            'description' => 'required|max:1000',
        ]);
    }
}
