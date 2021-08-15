@if ($errors->any())
    <div class="alert alert-danger">
        <strong>Error!</strong> 
        <ul>
            @foreach ($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif
<form action="{{ $task->id ? route('tasks.update', $task->id) : route('tasks.store' )}}" method="POST" >
    @csrf
    @if($task->id)
        @method('PATCH')
    @endif

    <div class="row">
        <div class="col-xs-12 col-sm-12 col-md-12">
            <div class="form-group">
                <strong>Name:</strong>
                <input type="text" data-testid="name" name="name" class="form-control" placeholder="Name" value="{{ $task->name }}">
            </div>
        </div>
        <div class="col-xs-12 col-sm-12 col-md-12">
            <div class="form-group">
                <strong>Description:</strong>
                <textarea data-testid="description"  class="form-control" row="3" name="description" placeholder="description">{{ $task->description }}</textarea>
            </div>
        </div>
        </div>
        <div class="col-xs-12 col-sm-12 col-md-12">
            <button data-testid="submit" type="submit" class="btn btn-primary">Submit</button>
        </div>
    </div>
</form>