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

class ManageTaskTest(BaseTestCases.BaseTest):

    edit_url = ''

    def test_signed_in_user_can_view_tasks(self):
        self.signed_in_user()

        if self.driver.current_url != config.path["tasks"]:
            self.driver.get(config.path["tasks"])
        
        self.assertIn('My Tasks', self.driver.page_source)

        self.logout_user()

    def test_add_task_form_requires_name_and_description(self):
        self.signed_in_user()

        self.driver.get(config.path["task_create"])

        name = self.driver.find_element_by_name("name")
        name.send_keys('')
        
        description = self.driver.find_element_by_name("description")
        description.send_keys('')

        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        self.wait_for_class_to_be_present('alert-danger')

        errors = {
            'name' : 'The name field is required.',
            'description' : 'The description field is required.',
        }

        self.assertIn(errors["name"], self.driver.page_source)
        self.assertIn(errors["description"], self.driver.page_source)

        self.logout_user()

    def test_signed_in_user_can_create_a_task(self):
        self.signed_in_user()

        self.driver.get(config.path["task_create"])

        task_name = Faker.get_task_name()
        task_description = Faker.get_task_description()

        name = self.driver.find_element_by_name("name")
        name.send_keys(task_name)
        
        description = self.driver.find_element_by_name("description")
        description.send_keys(task_description)

        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        self.wait_for_url_change(url = config.path["task_create"])

        self.assertIn(task_name, self.driver.page_source)
        self.assertIn(task_description, self.driver.page_source)

        self.logout_user()

    def add_valid_task(self, should_logout = False):
        self.signed_in_user()

        self.driver.get(config.path["task_create"])

        task_name = Faker.get_task_name()
        task_description = Faker.get_task_description()

        name = self.driver.find_element_by_name("name")
        name.send_keys(task_name)
        
        description = self.driver.find_element_by_name("description")
        description.send_keys(task_description)

        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        self.wait_for_url_change(url = config.path["task_create"])

        edit_container = self.driver.find_element_by_xpath("//p[text()='" + task_description + "']/following-sibling::p")
        edit_button = edit_container.find_element_by_tag_name('a')

        # save edit url of a valid task so we can use it later
        self.edit_url = edit_button.get_attribute('href')

        if should_logout:
            self.logout_user()

    def test_edit_task_form_requires_name_and_descrption(self):
        self.add_valid_task()

        self.driver.get(self.edit_url)

        name = self.driver.find_element_by_name("name")
        name.clear()
        
        description = self.driver.find_element_by_name("description")
        description.clear()

        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        self.wait_for_class_to_be_present('alert-danger')

        errors = {
            'name' : 'The name field is required.',
            'description' : 'The description field is required.',
        }

        self.assertIn(errors["name"], self.driver.page_source)
        self.assertIn(errors["description"], self.driver.page_source)

        self.logout_user()

    def test_signed_in_user_can_edit_a_task(self):
        self.add_valid_task()

        self.driver.get(self.edit_url)

        updated_task_name = Faker.get_task_name()
        updated_task_description = Faker.get_task_description()

        name = self.driver.find_element_by_name("name")
        old_name = name.text
        name.clear()
        name.send_keys(updated_task_name)
        
        description = self.driver.find_element_by_name("description")
        old_description = description.text
        description.clear()
        description.send_keys(updated_task_description)

        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.driver.execute_script("arguments[0].click();", submit_button)

        self.wait_for_url_change(url = self.edit_url)

        self.assertIn(updated_task_name, self.driver.page_source)
        self.assertIn(updated_task_description, self.driver.page_source)

        self.logout_user()
        
if __name__ == "__main__":
    unittest.main()