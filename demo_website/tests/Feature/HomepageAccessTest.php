<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class HomepageAccessTest extends TestCase
{
    use RefreshDatabase;
    
    /** @test */   
    public function guests_cannot_visit_the_homepage()
    {
        $this->get(route('home'))->assertRedirect('login');
    }

    /** @test */   
    public function signed_in_user_can_visit_the_homepage()
    {
        $this->signIn();

        $this->get(route('home'))->assertStatus(200);
    }
}
