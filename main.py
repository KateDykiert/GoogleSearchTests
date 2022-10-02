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


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get('https://www.google.com')
        self.home_page = page.HomePage(self.driver)
        self.home_page.accept_cookies()

    # def test_quick_language_change(self):
    #     self.home_page.quick_language_change()
    #     assert True

    def not_test_unsuccessful_sign_in(self):

        # checking if incorrect email is being handled correctly
        assert not self.home_page.sign_in("not.a.real.kasia.dykiert.email", "")

    def not_test_handling_0_results(self):

        # search phrase in the engine and click enter
        search_input = BasePageElement(self.driver, HomePageLocators.MAIN_SEARCH)
        search_input.set_text("tyhlvcejfliguhgvjocldfghnimldi nftgliudrvhmd;odrfinr")
        search_input.send_key(Keys.ENTER)

        result_page = page.SearchResultPage(self.driver)
        assert not result_page.any_results()
        # try:
        #     WebDriverWait(self.driver, 5).until(
        #             lambda driver: "Około 0 wyników" in driver.page_source
        #         )
        #     assert True
        # except TimeoutException:
        #     print("There is an incorrect number of results.")
        #     assert False

    def not_test_change_result_page(self):

        # search phrase in the engine and click enter
        search_input = BasePageElement(self.driver, HomePageLocators.MAIN_SEARCH)
        search_input.set_text("Apple")
        search_input.send_key(Keys.ENTER)

        # check if there is more than 0 results
        result_page = page.SearchResultPage(self.driver)
        assert result_page.any_results()
        # try:
        #     WebDriverWait(self.driver, 5).until(
        #             lambda driver: "Około 0 wyników" in driver.page_source
        #         )
        #     assert False
        # except TimeoutException:
        #     print("There is more than 0 results.")
        #     assert True

        # go to the next page
        result_page.go_to_next_page()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.driver.find_element(*SearchResultPageLocators.NEXT_PAGE).click()

        # check if correct page is being displayed
        assert result_page.is_page_number_matching(2)
        # try:
        #     WebDriverWait(self.driver, 5).until(
        #             lambda driver: "Strona 2 z około" in driver.page_source
        #         )
        #     assert True
        # except TimeoutException:
        #     print("Incorrect page number is being displayed.")
        #     assert False

        # go back to home page and check
        result_page.go_to_home_page()
        try:
            WebDriverWait(self.driver, 5).until(
                    lambda driver: driver.title == "Google"
                )
            assert True
        except TimeoutException:
            print("Has not returned to the home page")
            assert False

    def tearDown(self):
        # self.driver.close()
        pass


if __name__ == '__main__':

    unittest.main()
