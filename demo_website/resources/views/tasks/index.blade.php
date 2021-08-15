@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="text-right">
                <a class="btn btn-primary mb-3" href="{{ route('tasks.create')}}">Add Task</a>
            </div>
            <div class="card" data-testid="card">
                <div class="card-header">My Tasks</div>

                <div class="card-body">
                    @foreach($tasks as $task)
                    <h3>{{ $task->name}}</h3>
                    <p>{{ $task->description}}</p>
                    <p><a data-testid="edit-task" href="{{ route('tasks.edit', $task->id) }}">Edit</a></p>
                    <hr>
                    @endforeach
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
