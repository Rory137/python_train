import unittest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from group import Group


class test_add_group(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.wd = webdriver.Chrome(service=service)
        self.wd.implicitly_wait(500)

    def login_page(self, wd):
        wd.get("https://www.saucedemo.com/")
        url = wd.current_url
        print(url)

    def login_in_page(self, wd, group):
        username = wd.find_element("xpath", "//input[@id='user-name']")
        username.send_keys(group.username)

        password = wd.find_element("xpath", "//input[@id='password']")
        password.send_keys(group.password)

        login_button = wd.find_element("xpath", "//input[@id='login-button']")
        login_button.click()

    def add_item_to_cart(self, wd):
        add_to_cart_button = wd.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()

    def test_login_page(self):
        wd = self.wd
        self.login_page(wd)
        self.login_in_page(wd, Group(username="standard_user", password="secret_sauce"))
        self.add_item_to_cart(wd)
        time.sleep(10)


