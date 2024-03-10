import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class DribbleWebsiteResultPage:
    # Add locators

    SHOW_RESULTS = (By.CSS_SELECTOR, '')
    SEARCH_INPUT = (By.ID, 'search')

    # Initialize the Chrome browser
    def __init__(self, browser_driver):
        self.browser_driver = browser_driver

    # Identify the interaction methods
    def show_results_titles(self):
        results = self.browser_driver.find_elements(*self.SHOW_RESULTS)
        titles = [result.text for result in results]
        return titles

    def search_input_values(self):
        search_input = self.browser_driver.find_elements(*self.SEARCH_INPUT)
        item = search_input.get_attribute('value')
        return item

    def title(self):
        return self.browser_driver.title
