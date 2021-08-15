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

class LoginTest(BaseTestCases.BaseTest):

    def test_login_form_require_fields(self):
        self.driver.get(config.path['login'])

        self.wait_for_page_load()
    
        login_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", login_button)

        self.wait_for_class_to_be_present('invalid-feedback')

        errors = {
            'email' : 'The email field is required.',
            'password' : 'The password field is required.',
        }

        self.assertIn(errors["email"], self.driver.page_source)
        self.assertIn(errors["password"], self.driver.page_source)

    def test_user_can_login(self):
        self.driver.get(config.path['login'])

        self.wait_for_page_load()

        email = self.driver.find_element_by_id("email")
        email.send_keys(config.valid_user["email"])
        
        password = self.driver.find_element_by_id("password")
        password.send_keys(config.valid_user["password"])

        login_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", login_button)

        self.wait_for_url_change(url = config.path["login"])
        
        self.wait_for_page_load()
        
        dashboard_text = "You are logged in"

        self.assertIn(dashboard_text, self.driver.page_source)

        self.logout_user()

        self.wait_for_url_change(url = config.path["home"])

if __name__ == "__main__":
    unittest.main()