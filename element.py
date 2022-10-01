from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):

    def set_text(self, driver, locator, value):
        WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located(locator)
        )
        driver.find_element(*locator).clear()
        driver.find_element(*locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located(self.locator)
        )
        element = driver.find_element(self.locator)
        return element.get_attribute("value")

