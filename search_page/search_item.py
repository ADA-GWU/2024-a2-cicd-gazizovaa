from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DribbleWebsiteSearchPage:
    # Go to the website
    website_url = "https://dribbble.com/"

    # Add Locators
    SEARCH_INPUT = (By.ID, 'search')

    # Initialize the Chrome browser
    def __init__(self, browser_driver):
        self.browser_driver = browser_driver

    # Define interaction methods
    def load_page(self):
        self.browser_driver.get(self.website_url)

    def search_box(self, search_item):
        search_input = self.browser_driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(search_item + Keys.RETURN)
