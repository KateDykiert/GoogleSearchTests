from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def set_text(self, value):
        WebDriverWait(self.driver, 100).until(
            EC.visibility_of_element_located(self.locator)
        )
        self.driver.find_element(*self.locator).clear()
        self.driver.find_element(*self.locator).send_keys(value)

    def send_key(self, key):
        self.driver.find_element(*self.locator).send_keys(key)

    # def __get__(self, obj, owner):
    #     driver = obj.driver
    #     WebDriverWait(driver, 100).until(
    #         EC.visibility_of_element_located(self.locator)
    #     )
    #     element = driver.find_element(self.locator)
    #     return element.get_attribute("value")

