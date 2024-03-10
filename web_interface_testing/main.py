from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open a Chrome browser on a new tab
browser_driver = webdriver.Chrome()

# Go to the website
browser_driver.get("https://dribbble.com/")

# Wait for the search box element to be clickable
search_box = WebDriverWait(browser_driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='header"
                                                                                           "-search-input']")))

# Add search item in the box
search_item = input("Enter the searched item: ")
search_box.send_keys(search_item)

# Press Enter to perform the search
search_box.send_keys(Keys.ENTER)
