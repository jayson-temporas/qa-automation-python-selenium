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

class ForgotPasswordTest(BaseTestCases.BaseTest):

    def test_forgot_password_form_require_field(self):
        self.driver.get(config.path['forgot_password'])

        self.wait_for_page_load()
    
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        self.wait_for_class_to_be_present('invalid-feedback')

        error = 'The email field is required.'

        self.assertIn(error, self.driver.page_source)

    def test_user_can_submit_forgot_password_request(self):
        self.driver.get(config.path['forgot_password'])

        self.wait_for_page_load()

        email = self.driver.find_element_by_id("email")
        email.send_keys(config.valid_user["email"])

        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)
        
        self.wait_for_class_to_be_present('alert-success')

        info_text = "We have emailed your password reset link!"

        self.assertIn(info_text, self.driver.page_source)

if __name__ == "__main__":
    unittest.main()