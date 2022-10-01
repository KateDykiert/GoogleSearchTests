from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import page
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

    def test_unsuccessful_sign_in(self):
        assert not self.home_page.sign_in("not.a.real.kasia.dykiert.email", "")

    def test_search_phrase(self):


    def tearDown(self):
        # self.driver.close()
        pass

if __name__ == '__main__':

    unittest.main()