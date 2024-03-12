import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time


class DribbleSearchFeatureTest(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver instance for Chrome browser
        self.browser_driver = webdriver.Chrome()
        # Wait for the elements implicitly during the specified time
        self.browser_driver.implicitly_wait(5)
        # Go to the search page on the Dribble application
        self.browser_driver.get("https://dribbble.com/search")

    def test_search_mechanism(self):
        # The searched item
        search_for_design = "chat app ui"

        try:
            # Wait for clickable search input
            search_input = WebDriverWait(self.browser_driver, 5).until(EC.element_to_be_clickable((By.ID, "search")))
            # Waiting for the search input to become clickable
            search_input.send_keys(search_for_design)
            time.sleep(3)

            # Initiate the searching with the Enter key
            search_input.send_keys(Keys.RETURN)
            time.sleep(3)

            # Verify the searched item in page source
            assert search_for_design in self.browser_driver.page_source

        except StaleElementReferenceException:
            # Wait for the page to reload or element to become clickable again
            search_input = WebDriverWait(self.browser_driver, 5).until(EC.element_to_be_clickable((By.ID, "search")))
            search_input.send_keys(search_for_design)
            time.sleep(3)

            search_input.send_keys(Keys.RETURN)
            time.sleep(3)

            assert search_for_design in self.browser_driver.page_source

    def tearDown(self):
        # Close webdriver after test
        self.browser_driver.quit()


if __name__ == "__main__":
    # Run a test case
    unittest.main()
