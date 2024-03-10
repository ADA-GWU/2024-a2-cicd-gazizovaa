import pytest
from selenium import webdriver


@pytest.fixture
def config_browser():
    # Initialize the ChromeDriver instance
    browser_driver = webdriver.Chrome()

    # Set an implicit weight of 20 seconds before raising an exception
    browser_driver.implicitly_wait(20)

    # Return the injected webdriver instance
    yield browser_driver

    # Quit the webdriver instance for cleanup
    browser_driver.quit()
