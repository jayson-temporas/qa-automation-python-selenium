#!/usr/bin/env python

driver = "Chrome"

mobile_test = False
mobile_name = "iPhone 6/7/8"

basic_info = {
    "name" : 'jay temp',
    "email" : 'jaytemp@email.com',
    "password" : 'password',
}

valid_user = {
    "email" : "test@email.com",
    "password" : "password",
}

path = {
    "host": 'http://localhost:8000',
    "register": 'http://localhost:8000/register',
    "login": 'http://localhost:8000/login',
    "logout": 'http://localhost:8000/logout',
    "home": 'http://localhost:8000/home',
    "forgot_password": 'http://localhost:8000/password/reset',
    "tasks": 'http://localhost:8000/tasks',
    "task_create": 'http://localhost:8000/tasks/create',
    "task_edit": 'http://localhost:8000/tasks/1/edit',
}

drivers = {
    'chrome': './drivers/chromedriver',
    'firefox': './drivers/geckodriver',
    'safari': '/usr/bin/safaridriver',
}


sleep_on_wait = False