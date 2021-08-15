import config
import random

# Simple Faker class to populate our app content
# You can download Python Faker package for more complex usage
# pip install Faker

class Faker:
    
    @staticmethod
    def get_name():
        random_number =  str(random.randint(0,99999))
        return config.basic_info['name'] + random_number
    
    @staticmethod
    def get_email():
        random_number =  str(random.randint(0,99999))
        return config.basic_info['email'] + random_number
    
    def get_task_name():
        random_number =  str(random.randint(0,99999))
        return 'Task ' + random_number

    def get_task_description():
        random_number =  str(random.randint(0,99999))
        return 'Task  description ' + random_number