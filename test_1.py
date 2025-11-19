import unittest
import pytest
import time
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from group import Group
from application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    def teardown():
        fixture.destroy()
    request.addfinalizer(teardown)
    return fixture

# class test_add_group(unittest.TestCase):
    # def setUp(self):
        #self.app = Application()

    # def wait_load(self, time):
    #     wd = self.wd
    #     wait = WebDriverWait(wd, time)
    #     return wait
    #
    # def scroll_to_element(self, element):
    #     wd = self.wd
    #     wd.execute_script("arguments[0].scrollIntoView(true);", element)
    #     time.sleep(0.5)
    #
    #
    # def login_page(self):
    #     wd = self.wd
    #     wd.get("https://www.saucedemo.com/")
    #     url = wd.current_url
    #     print(url)
    #
    # def login_in_page(self, group):
    #     wd = self.wd
    #     self.login_page(wd)
    #     username = wd.find_element("xpath", "//input[@id='user-name']")
    #     username.send_keys(group.username)
    #
    #     password = wd.find_element("xpath", "//input[@id='password']")
    #     password.send_keys(group.password)
    #
    #     login_button = wd.find_element("xpath", "//input[@id='login-button']")
    #     login_button.click()
    #
    # def add_item_to_cart(self):
    #     wd = self.wd
    #     # inventory_item = wd.EC.presence_of_all_elements_located(By.CLASS_NAME, "inventory_item")
    #     inventory_item = self.wait_load(wd,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    #     item_choice = inventory_item[:6]
    #     random_item = random.choice(item_choice)
    #     item_name = random_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    #     add_to_cart_button = random_item.find_element(By.CLASS_NAME, "btn_primary")
    #     add_to_cart_button.click()
    #     self.scroll_to_element(wd, random_item)
    #     print(f'Товар {item_name} был добавлен в корзину')

    # add_to_cart_button = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_primary")))
       # random_add_basket = add_to_cart_button[:6]
       # random_add_to_cart_button = random.choice(random_add_basket)
       # random_add_to_cart_button.click()

def test_login_page(app):
    app.login_in_page(Group(username="standard_user", password="secret_sauce"))
    app.add_item_to_cart()
    time.sleep(5)




