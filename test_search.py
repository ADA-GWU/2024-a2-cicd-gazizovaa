import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class DribbleWebsiteSearchTest(unittest.TestCase):
    def setUp(self):
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.implicitly_wait(10)
        self.browser_driver.get("https://dribbble.com/search")

    def test_search_app_design(self):
        search_design = "chat app ui"
        search_input = WebDriverWait(self.browser_driver, 10).until(EC.element_to_be_clickable((By.ID, "search")))
        search_input.send_keys(search_design)
        time.sleep(5)
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)
        assert search_design in self.browser_driver.page_source

    def tearDown(self):
        self.browser_driver.quit()


if __name__ == "__main__":
    unittest.main()
