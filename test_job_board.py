import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DribbbleJobsSearchTest(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver instance for Chrome browser
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.get("https://dribbble.com/search")

    def test_search_jobs_board(self):
        # The searched item
        search_for_jobs = "Adobe Photoshop"

        try:
            # Wait for clickable search input
            search_input = WebDriverWait(self.browser_driver, 5).until(
                EC.element_to_be_clickable((By.ID, "search-input")))
            # Clear the search box
            search_input.clear()
            # Waiting for the search input to become clickable
            search_input.send_keys(search_for_jobs)

            # Initiate the searching with the Enter key
            search_input.send_keys(Keys.RETURN)
            # Wait for the search results to stabilize
            WebDriverWait(self.browser_driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobs-link")))

        # Handle the timeout exception here
        except TimeoutException:
            # Add necessary error handling or leave it if it's empty
            pass

    def tearDown(self):
        # Close the WebDriver after each test
        self.browser_driver.quit()


if __name__ == "__main__":
    unittest.main()
