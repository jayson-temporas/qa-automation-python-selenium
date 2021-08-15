<?php

/** @var \Illuminate\Database\Eloquent\Factory $factory */

use App\Task;
use Faker\Generator as Faker;

$factory->define(Task::class, function (Faker $faker) {
    return [
        'name' => $faker->sentence(4),
        'description' => $faker->sentence(8),
        'user_id' => factory(App\User::class)
    ];
});
