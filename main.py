from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import page
from element import BasePageElement
from locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get('https://www.google.com')
        self.home_page = page.HomePage(self.driver)
        self.home_page.accept_cookies()

    # def test_quick_language_change(self):
    #     self.home_page.language_change()
    #     assert True

    def not_test_unsuccessful_sign_in(self):
        assert not self.home_page.sign_in("not.a.real.kasia.dykiert.email", "")

    def test_get_any_results(self):

        # search phrase in the engine and click enter
        search_input = BasePageElement(HomePageLocators.MAIN_SEARCH)
        search_input.set_text(self.driver, "kasia")
        search_input.send_key(self.driver, Keys.ENTER)

        # check if there is more than 0 results
        try:
            WebDriverWait(self.driver, 5).until(
                    lambda driver: "Około 0 wyników" in driver.page_source
                )
            assert False
        except TimeoutException:
            print("There is more than 0 results.")
            assert True

    def tearDown(self):
        # self.driver.close()
        pass


if __name__ == '__main__':

    unittest.main()
