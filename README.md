[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/jwssRZI4)

## Assignment #2. Automation of the service delivery
## Prerequisites

## 1. Install Python
* Make sure that Python is installed in your machine. Othweise, please refer to this page .[Download Python](https://www.python.org/);
* You should have Python editor/IDE depending on your choise. Convenient choises include .[PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows) and .[Visual Studio Code](https://code.visualstudio.com/download);
* Download the latest Python version . This assignmented required Python 3.8 or higher (mine is Python 3.11.8).

## 2. Install Selenium 
#### Install Selenium using Python's package manager. Open the command prompt or terminal and type the following command:
```
pip install selenium
```
## 3. Install Python Environment
#### You are required to use pipenv. To install pipenv, run the following command from terminal or command line:
```
pip install pipenv
```

## 4. SetUp Webdriver
* You will neeed to install the latests versions of Google Chrome and Mozilla FireFox. You can prefer to use other browsers with Selenium WbeDriver;
* You will need to install the latests versions of the WebDriver executables for these browsers: .[ChromeDriver](https://chromedriver.chromium.org/downloads) for Chrome and .[geckodriver](https://github.com/mozilla/geckodriver/releases) for FireFox.

## 5. SetUp WebDriver for Windows OS
#### In my case, I used ChromeDriver. To install ChromeDriver:
**Step 1:** Go to .[ChromeDriver - WebDriver for Chrome - Downloads page](https://chromedriver.chromium.org/downloads) to install the latest Wbedriver executables;

**Step 2:** Click on the **The Chrome for Testing availability dashboard**, indicated by redline under **Current Releases**;

**Step 3:** Depending on your Chrome version, refer to one of the listed channels. In my case, I selected **Stable**;

**Notes:** Type ```chrome://version/``` to learn the version of your Chrome you use.

**Step 4:** Select WebDriver from **Binary ** column corresponding to your OS. I selected ChromeDriver for **win64** and install this [URL](https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/win64/chromedriver-win64.zip). The link will be download as zip file and unzip it;

**Step 5:** Locate the chromedriver.exe from the folder to a place on your machine. I copied chromedriver and pasted it in the C:\Program Files\Google\Chrome\Application. Also, don't forget to add path to the Environment Variables, as C:\Program Files\Google\Chrome path, under System Variables -> Path.

### The name of the application I selected is Dribble (https://dribbble.com/search)

## 6. Run Python Scripts
### Run test_search_feature.py file
* Just click on the python script and right click, click **Run**. It will showw the test case process and the result:

```
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
```

### Run test_job_board.py file
* Just click on the python script and right click, click **Run**. It will showw the test case process and the result:

```
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
```


  




