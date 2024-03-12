import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class DribbleWebsiteEditProfileTest(unittest.TestCase):
    def setUp(self):
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.implicitly_wait(5)
        self.browser_driver.get("https://dribbble.com/search")

    def test_edit_profile(self):
        self.browser_driver.find_element_by_link_text("Open Profile")
        time.sleep(5)

        edit_profile_btn = WebDriverWait(self.browser_driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='btn2 btn2--tertiary profile-action-item'][href='https://dribbble.com/account/profile']")))
        time.sleep(7)

        edit_profile_url = self.browser_driver.current_url
        assert edit_profile_url == "https://dribbble.com/account/profile"


if __name__ == "__main__":
    unittest.main()


