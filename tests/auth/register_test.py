import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import config
from BaseTestCases import BaseTestCases
from Faker import Faker

class RegisterTest(BaseTestCases.BaseTest):

    def test_register_form_require_fields(self):
        self.driver.get(config.path['register'])

        self.wait_for_page_load()
    
        register_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", register_button)

        errors = {
            'name' : 'The name field is required.',
            'email' : 'The email field is required.',
            'password' : 'The password field is required.',
        }

        self.wait_for_class_to_be_present('invalid-feedback')

        self.assertIn(errors["name"], self.driver.page_source)
        self.assertIn(errors["email"], self.driver.page_source)
        self.assertIn(errors["password"], self.driver.page_source)
    
    def test_register_form_passwords_should_match(self):
        self.driver.get(config.path['register'])

        self.wait_for_page_load()

        data = {
            'password' : 'password123',
            'password_confirmation' : 'password111',
        }

        password = self.driver.find_element_by_id("password")
        password.send_keys(data["password"])
        
        password_confirmation = self.driver.find_element_by_id("password-confirm")
        password_confirmation.send_keys(data["password_confirmation"])

        register_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", register_button)

        self.wait_for_class_to_be_present('invalid-feedback')

        error = 'The password confirmation does not match.'
        form  = self.driver.find_element_by_xpath("//form[@action='"+config.path['register']+"']")

        self.assertIn(error, form.text)

    def test_user_can_register(self):
        self.driver.get(config.path['register'])

        self.wait_for_page_load()
    
        first_name = self.driver.find_element_by_id("name")
        first_name.send_keys(Faker.get_name())

        email = self.driver.find_element_by_id("email")
        email.send_keys(Faker.get_email())
        
        password = self.driver.find_element_by_id("password")
        password.send_keys(config.basic_info["password"])
        
        password_confirmation = self.driver.find_element_by_id("password-confirm")
        password_confirmation.send_keys(config.basic_info["password"])

        register_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", register_button)

        self.wait_for_url_change(url = config.path["register"])
        
        dashboard_text = "You are logged in"

        self.assertIn(dashboard_text, self.driver.page_source)

        self.logout_user()

if __name__ == "__main__":
    unittest.main()