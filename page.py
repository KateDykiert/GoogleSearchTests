from locator import *
from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 100).until(
            EC.visibility_of_element_located(locator)
        )

    def sign_in(self, login, password):

        # click "sign in" button
        sign_in = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a")
        sign_in.click()

        # input email and click "next" button
        email_input = BasePageElement()
        email_input.set_text(self.driver, SignInPageLocators.EMAIL_OR_PHONE_INPUT, login)
        next_button = self.driver.find_element(*SignInPageLocators.NEXT_BUTTON).click()

        # wait for the error to show up, if not - accept
        try:
            WebDriverWait(self.driver, 5).until(
                lambda driver: "Nie możemy znaleźć takiego konta Google" in driver.page_source
            )
            return False
        except TimeoutException:
            print("Provided login has been accepted.")

        # input password and click next
        password_input = BasePageElement()
        password_input.set_text(self.driver, SignInPageLocators.PASSWORD_INPUT, password)
        next_button.click()

        # wait for the error to show up, if not - accept
        try:
            WebDriverWait(self.driver, 5).until(
                lambda driver: "Nieprawidłowe hasło. Spróbuj jeszcze raz lub kliknij „Nie pamiętasz hasła?”, "
                               "by je zresetować." in driver.page_source
            )
            return False
        except TimeoutException:
            print("Provided password has been accepted.")

        # check if the user go redirected to home page
        time.sleep(5)
        if self.driver.title == "Google":
            return True
        return False


class HomePage(BasePage):

    def accept_cookies(self):
        accept_all_button = self.wait_for_element(HomePageLocators.ACCEPT_ALL_COOKIES)
        accept_all_button.click()

    def language_change(self):
        suggested_language = self.driver.find_element(*HomePageLocators.SUGGESTED_LANGUAGE)
        suggested_language.click()
