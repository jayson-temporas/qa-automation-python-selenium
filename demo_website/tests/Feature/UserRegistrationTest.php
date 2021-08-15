<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class UserRegistrationTest extends TestCase
{
    use RefreshDatabase;
    
    /** @test */   
    public function signed_in_user_cannot_visit_the_registration_page()
    {
        $this->signIn();

        $this->get(route('register'))->assertRedirect('home');

        $attributes = factory('App\User')->raw();

        $this->post(route('register'), $attributes)->assertStatus(302);
    }

    /** @test */   
    public function signed_in_user_cannot_register_a_new_user()
    {
        $this->signIn();

        $attributes = factory('App\User')->raw();

        $this->post(route('register'), $attributes)->assertStatus(302);
    }

    /** @test */
    public function a_user_should_be_able_to_register()
    {
        $attributes = factory('App\User')->raw(['password' => '12345678']);
        $attributes['password_confirmation'] = '12345678';

        $this->post(route('register'), $attributes)->assertSessionHasNoErrors();
    }

     /** @test */
    public function a_user_requires_an_email()
    {
        $attributes = factory('App\User')->raw(['email' => '']);

        $this->post(route('register'), $attributes)->assertSessionHasErrors('email');
    }

    /** @test */
    public function a_user_requires_a_name()
    {
        $attributes = factory('App\User')->raw(['name' => '']);

        $this->post(route('register'), $attributes)->assertSessionHasErrors('name');
    }

    /** @test */
    public function a_user_requires_a_password()
    {
        $attributes = factory('App\User')->raw(['password' => '']);

        $this->post(route('register'), $attributes)->assertSessionHasErrors('password');
    }

     /** @test */
    public function a_user_requires_a_valid_email()
    {
        $attributes = factory('App\User')->raw(['email' => 'notvalid']);

        $this->post(route('register'), $attributes)->assertSessionHasErrors('email');

        $attributes = factory('App\User')->raw(['email' => 'valid@email.com']);
        $attributes['password'] = '12345678';
        $attributes['password_confirmation'] = '12345678';

        $this->post(route('register'), $attributes)->assertSessionDoesntHaveErrors('email');
    }

    /** @test */
    public function a_user_password_should_match_confirm_password()
    {
        $attributes = factory('App\User')->raw(['password' => '12345678']);

        $attributes['password_confirmation'] = '11223344';

        $this->post(route('register'), $attributes)->assertSessionHasErrors('password');

        $attributes = factory('App\User')->raw(['password' => '12345678']);

        $attributes['password_confirmation'] = '12345678';

        $this->post(route('register'), $attributes)->assertSessionHasNoErrors();
    }

    /** @test */
    public function a_user_password_should_be_atleast_8_characters()
    {
        $attributes = factory('App\User')->raw(['password' => '123456']);
        $attributes['password_confirmation'] = '123456';

        $this->post(route('register'), $attributes)->assertSessionHasErrors('password');

        $attributes = factory('App\User')->raw(['password' => '12345678']);
        $attributes['password_confirmation'] = '12345678';

        $this->post(route('register'), $attributes)->assertSessionHasNoErrors();
    }

}
