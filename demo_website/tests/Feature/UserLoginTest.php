<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;
use Illuminate\Support\Facades\Hash;

class UserLoginTest extends TestCase
{
    use RefreshDatabase;
    
    /** @test */   
    public function signed_in_user_cannot_visit_the_login_page()
    {
        $this->signIn();

        $this->get(route('login'))->assertRedirect('home');
    }

     /** @test */
    public function login_form_requires_an_email()
    {
        $attributes = factory('App\User')->raw(['email' => '']);

        $this->post(route('login'), $attributes)->assertSessionHasErrors('email');
    }

    /** @test */
    public function login_form_requires_a_password()
    {
        $attributes = factory('App\User')->raw(['password' => '']);

        $this->post(route('login'), $attributes)->assertSessionHasErrors('password');
    }

    /** @test */
    public function a_user_can_signed_in_with_valid_credentials()
    {
        $attributes = factory('App\User')->raw(['password' => '12345678', 'email' => 'user@email.com']);

        $this->post(route('login'), $attributes)->assertSessionHasErrors('email');

        $validUser = factory('App\User')->create([
            'password' => Hash::make('12345678')
        ]);

        $validAttributes = factory('App\User')->raw(['password' => '12345678', 'email' => $validUser->email]);

        $this->post(route('login'), $validAttributes)->assertSessionHasNoErrors();

        $this->assertAuthenticatedAs($validUser);
    }

     /** @test */
    public function a_signed_in_user_can_logout()
    {
        $this->post(route('logout'))->assertStatus(302);

        $user = $this->signIn();

        $this->post(route('logout'))->assertRedirect('/');
    }

}
