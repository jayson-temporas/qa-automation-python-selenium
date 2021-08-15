# QA Automation using Selenium and Python

This is a sample QA Automation project using selenium and python. 

## Setup

### Python and Selenium

- Should have python 3 and selenium installed
- Download webdrivers for Chrome and Firefox and update the config path
- Find your safari browser webdriver, usually located at /usr/bin/safaridriver, update config path if necessary

### Demo Website

- Should have PHP installed
- Create a .env file and update env variables
- Create demo_website/database/database.sqlite file 

### Add config.py for our test env variables

```
cp tests/config.test.py tests/config.py
```

## Test Coverage

- Login Feature Test
    - login form require fields
    - valid user should be able to log in
- Register Feature Test
    - registration form require fields
    - password and password confirmation should match
    - a valid form should be able to register a user
- Forgot Password Feature Test
    - forgot password form require field
    - valid form should send an email instruction to reset a password
- Task Feature Test
    - Task Access Test
        - Guest user cant view the task list
        - Guest user cant add a task
        - Guest user cant edit a task
        - Guest user cant delete a task
    - Manage Task Test
        - Task form require fields
        - Valid add task form should create a task
        - Valid edit task form should update a task

## Run Tests

Run tests on Desktop

```
python app.py --chrome
```

```
python app.py --firefox
```

```
python app.py --safari
```

Run tests on Mobile Emulator

```
python app.py --chrome --mobile
```

```
python app.py --firefox --mobile
```

Safari does not support mobile emulator on test automation
