<div style="height:80px;padding:20px;width:100%;background: -webkit-linear-gradient(to right, #2C5364, #203A43, #0F2027);  background: linear-gradient(to right, #2C5364, #203A43, #0F2027);">
    <h1 style="color:#fff;">Hello {{ $user->name }}</h1>    
</div>
<div style="padding:20px;">
    You have a total of {{ count($tasks) }} {{ \Illuminate\Support\Str::plural('task', count($tasks))}}.
    <br><br>
    Regards, <br>
    <h1 style="color:#000;">The Best Team</h1>
    <hr>
</div>
<div style="height:30px;padding:10px;padding-top:20px;text-align:center;width:100%;background: -webkit-linear-gradient(to right, #2C5364, #203A43, #0F2027);  background: linear-gradient(to right, #2C5364, #203A43, #0F2027);">
    <div style="color:#fff;font-size:16px;">TBT&copy; 2021</div>    
</div>