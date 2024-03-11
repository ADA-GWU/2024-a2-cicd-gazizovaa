import unittest
from selenium import webdriver
import time


class DribbleWebsiteLoginTest(unittest.TestCase):
    def setUp(self):
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.implicitly_wait(10)
        self.browser_driver.get("https://dribbble.com/search")

    def test_login_valid(self):
        self.browser_driver.find_element_by_link_text("")

