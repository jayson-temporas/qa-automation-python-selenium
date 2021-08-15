import unittest
from selenium import webdriver
import config
import time
import os
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseTestCases:
    
    class BaseTest(unittest.TestCase):
        @classmethod
        def setUp(self):
            # reset db before running each test
            os.system("php ../demo_website/artisan migrate:fresh --seed --quiet")

        @classmethod
        def setUpClass(self):
            print("Openning Browser " + config.driver)

            if config.driver == 'Chrome':
                if config.mobile_test:
                    mobile_emulation = { "deviceName": config.mobile_name }
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
                    self.driver = webdriver.Chrome(executable_path=config.drivers['chrome'], options=chrome_options)
                else:
                    self.driver = webdriver.Chrome(executable_path=config.drivers['chrome'])
                    self.driver.maximize_window()
            elif config.driver == 'Safari':
                if config.mobile_test:
                    # safari mobile emulator is not supported
                    self.driver = webdriver.Safari(executable_path=config.drivers['safari'])
                else:
                    self.driver = webdriver.Safari(executable_path=config.drivers['safari'])
                    self.driver.maximize_window()
            elif config.driver == 'Firefox':
                if config.mobile_test:
                    user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
                    profile = webdriver.FirefoxProfile() 
                    profile.set_preference("general.useragent.override", user_agent)
                    self.driver = webdriver.Firefox(executable_path=config.drivers['firefox'], firefox_profile=profile)
                    self.driver.set_window_size(360,640)
                else:
                    self.driver = webdriver.Firefox(executable_path=config.drivers['firefox'])
                    self.driver.maximize_window()


        @classmethod
        def tearDownClass(self):
            print("Closing Browser " + config.driver)
            self.driver.quit()

        def ajax_complete(self, driver):
            try:
                return 0 == driver.execute_script("return jQuery.active")
            except WebDriverException:
                pass

        def load_complete(self, driver):
            try:
                return 'complete' == driver.execute_script("return document.readyState")
            except WebDriverException:
                pass

        def wait_for_ajax(self):
            if config.sleep_on_wait:
                time.sleep(3)
            else:
                WebDriverWait(self.driver, 30).until(
                self.ajax_complete,  "Timeout waiting for ajax to load")

        def wait_for_page_load(self):
            if config.sleep_on_wait:
                time.sleep(3)
            else:
                WebDriverWait(self.driver, 30).until(
                self.load_complete,  "Timeout waiting for page to load")

        def wait_for_url_change(self, url):
            if config.sleep_on_wait:
                time.sleep(3)
            else:
                WebDriverWait(self.driver, 30).until(
                EC.url_changes(url))

        def wait_for_class_to_be_present(self, class_name = ''):
            if config.sleep_on_wait:
                time.sleep(3)
            else:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "." + class_name)))
        
        def wait_for_class_to_be_visible(self, class_name = ''):
            if config.sleep_on_wait:
                time.sleep(3)
            else:
                WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "." + class_name)))

        def logout_user(self):
            if (config.mobile_test):
                navbar_toggler = self.driver.find_element_by_xpath("//button[@class, 'navbar-toggler')]")
                navbar_toggler.click()
                
            navbar_dropdown = self.driver.find_element_by_id('navbarDropdown')
            navbar_dropdown.click()

            logout_button =  self.driver.find_element_by_xpath("//a[contains(text(), 'Logout')]")
            
            if logout_button:
                logout_button.click()
                self.wait_for_url_change(url = config.path["home"])

        def signed_in_user(self):
            if self.driver.current_url != config.path["login"]:
                self.driver.get(config.path['login'])
                
            self.wait_for_page_load()

            email = self.driver.find_element_by_id("email")
            email.send_keys(config.valid_user["email"])
            
            password = self.driver.find_element_by_id("password")
            password.send_keys(config.valid_user["password"])

            login_button = self.driver.find_element_by_xpath("//button[@type='submit']")
            self.driver.execute_script("arguments[0].click();", login_button)
            
            self.wait_for_url_change(url = config.path["login"])