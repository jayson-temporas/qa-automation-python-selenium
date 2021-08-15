@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card" data-testid="card">
                <div class="card-header">Add Task</div>

                <div class="card-body">
                    @include('tasks.partial.form')
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
