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

class TaskAccessTest(BaseTestCases.BaseTest):

    def test_guest_user_cannot_view_task_list(self):
        self.driver.get(config.path["tasks"])

        self.wait_for_url_change(url = config.path["tasks"])

        self.assertEquals(self.driver.current_url, config.path["login"])

    def test_guest_user_cannot_view_add_task_form(self):
        self.driver.get(config.path["task_create"])

        self.wait_for_url_change(url = config.path["task_create"])

        self.assertEquals(self.driver.current_url, config.path["login"])

    def test_guest_user_cannot_view_edit_task_form(self):
        self.driver.get(config.path["task_edit"])

        self.wait_for_url_change(url = config.path["task_edit"])

        self.assertEquals(self.driver.current_url, config.path["login"])


if __name__ == "__main__":
    unittest.main()