import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DribbbleJobsSearchTest(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver (assuming Chrome WebDriver here)
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.get("https://dribbble.com/search")  
    def tearDown(self):
        # Close the WebDriver after each test
        self.browser_driver.quit()

    def test_search_adobe_photoshop_jobs(self):
        # The searched item
        search_for_adobe_photoshop_jobs = "Adobe Photoshop"

        try:
            # Wait for clickable search input
            search_input = WebDriverWait(self.browser_driver, 5).until(
                EC.element_to_be_clickable((By.ID, "search-input")))
            # Clear the search box
            search_input.clear()
            # Waiting for the search input to become clickable
            search_input.send_keys(search_for_adobe_photoshop_jobs)

            # Initiate the searching with the Enter key
            search_input.send_keys(Keys.RETURN)
            # Wait for the search results to stabilize
            WebDriverWait(self.browser_driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobs-link")))

        except TimeoutException:
            # Handle the timeout exception here
            pass  # You can add any necessary error handling or logging here, or leave it empty

        # Add your assertions or further test steps here


if __name__ == "__main__":
    unittest.main()
