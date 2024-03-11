import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class DribbleWebsiteSearchTest(unittest.TestCase):
    def setUp(self):
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.implicitly_wait(30)
        self.browser_driver.get("https://dribbble.com/")

    def test_search_box(self):
        search_query = "design"
        search_input = self.browser_driver.find_element_by_name("q")
        search_input.send_keys(search_query + Keys.RETURN)
        time.sleep(2)

        get_search_results = self.browser_driver.find_elements_by_class_name("shot-thumbnail")
        self.assertGreater(len(get_search_results), 0)

    def tearDown(self):
        self.browser_driver.quit()


if __name__ == "__main__":
    unittest.main()
