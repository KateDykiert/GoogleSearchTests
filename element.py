from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):

    def __init__(self, locator):
        self.locator = locator

    def set_text(self, driver, value):
        WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located(self.locator)
        )
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def send_key(self, driver, key):
        driver.find_element(*self.locator).send_keys(key)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located(self.locator)
        )
        element = driver.find_element(self.locator)
        return element.get_attribute("value")

