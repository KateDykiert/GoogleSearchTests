# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GoogleSearch(unittest.TestCase):

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('https://www.google.com')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':

    unittest.main()