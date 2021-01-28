import time
from util.secrets import *


def login(browser):
    browser.get('https://www.instagram.com/')
    time.sleep(5)
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    login_button = browser.find_element_by_css_selector("button")

    username.send_keys(name)
    password.send_keys(pw)
    login_button.click()

    time.sleep(5)
