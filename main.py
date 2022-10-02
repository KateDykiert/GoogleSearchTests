from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class GoogleSearch(unittest.TestCase):

    def setUp(self):

        # driver and home_page declaration
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.get('https://www.google.com')
        self.home_page = page.HomePage(self.driver)
        self.home_page.accept_cookies()

    def test_explicit_contents(self):

        print("\nTEST - Explicit content switch")

        # search phrase in the engine
        self.home_page.search("marvel cinematic universe")

        # check if explicit search is correctly on or off
        result_page = page.SearchResultPage(self.driver)
        result_page.switch_explicit_search()
        assert result_page.is_safe_search_on(), "SafeSearch failed to switch on."
        result_page.switch_explicit_search()
        assert not result_page.is_safe_search_on(), "SafeSearch failed to switch off"

    def test_change_result_page(self):

        print("\nTEST - Search and change page.")

        # search phrase in the engine
        self.home_page.search("Apple")

        # check if there is more than 0 results
        result_page = page.SearchResultPage(self.driver)
        assert result_page.any_results(), "No results were found."

        # go to the next page
        result_page.go_to_next_page()

        # check if correct page is being displayed
        assert result_page.is_page_number_matching(2), "Incorrect page number is being displayed."

        # go back to home page and check
        result_page.go_to_home_page()
        try:
            WebDriverWait(self.driver, 5).until(
                    lambda driver: driver.title == "Google"
                )
            assert True
        except TimeoutException:
            assert False, "Has not returned to the home page."

    def test_handling_0_results(self):

        print("\nTEST - Handling 0 results.")

        # search phrase in the engine
        self.home_page.search("tyhlvcejfliguhgvjocldfghnimldi nftgliudrvhmd;odrfinr")

        # see if 0 results is being handled properly
        result_page = page.SearchResultPage(self.driver)
        assert not result_page.any_results(), "Failed to show number or results as 0."

    def test_unsuccessful_sign_in(self):

        print("\nTEST - Unsuccessful sign in handling.")

        # checking if incorrect email is being handled correctly
        assert not self.home_page.sign_in("not.a.real.kasia.dykiert.email", ""), \
            "Unregistered user was permitted to log in."

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':

    unittest.main()
