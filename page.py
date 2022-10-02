from locator import *
from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):

        """
        Waits for the provided WebElement to be present on the DOM of a page and visible.

        :param locator: tuple of 2 elements - (selenium By, string) E.g. (By.NAME, "Passwd")
        :return: WebElement
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def sign_in(self, login, password):

        """
        Performs full sign in from the home page with provided credentials.

        :param login: string
        :param password: string
        :return: Boolean - True if sign in has been successful. Otherwise, returns False.
        """
        # click "sign in" button
        print("Clicking the 'Sign in' button.")
        sign_in = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a")
        sign_in.click()

        # input email and click "next" button
        email_input = BasePageElement(self.driver, SignInPageLocators.EMAIL_OR_PHONE_INPUT)
        print("Providing login.")
        email_input.set_text(login)
        next_button = self.driver.find_element(*SignInPageLocators.NEXT_BUTTON).click()

        # wait for the error to show up, if not - accept
        try:
            WebDriverWait(self.driver, 5).until(
                    lambda driver: "Nie możemy znaleźć takiego konta Google" in driver.page_source
                )
            print("Provided login has been rejected.")
            return False
        except TimeoutException:
            print("Provided login has been accepted.")

        # input password and click next
        password_input = BasePageElement(self.driver, SignInPageLocators.PASSWORD_INPUT)
        print("Providing password.")
        password_input.set_text(password)
        next_button.click()

        # wait for the error to show up, if not - accept
        try:
            WebDriverWait(self.driver, 5).until(
                    lambda driver: "Nieprawidłowe hasło. Spróbuj jeszcze raz lub kliknij „Nie pamiętasz hasła?”, "
                               "by je zresetować." in driver.page_source
                )
            print("Provided password has been rejected.")
            return False
        except TimeoutException:
            print("Provided password has been accepted.")

        # check if the user go redirected to home page
        time.sleep(5)
        if self.driver.title == "Google":
            print("User got redirected to home page.")
            return True
        print("Failed to get redirected.")
        return False


class HomePage(BasePage):

    def accept_cookies(self):

        """
        Accepts cookies of Google.
        """
        accept_all_button = self.wait_for_element(HomePageLocators.ACCEPT_ALL_COOKIES)
        accept_all_button.click()

    # def quick_language_change(self):
    #     suggested_language = self.driver.find_element(*HomePageLocators.SUGGESTED_LANGUAGE)
    #     suggested_language.click()

    def search(self, phrase):

        """
        Performs a Google search of a provided phrase.

        :param phrase: string
        """
        print("Searching for '{}'.".format(phrase))
        search_input = BasePageElement(self.driver, HomePageLocators.MAIN_SEARCH)
        search_input.set_text(phrase)
        search_input.send_key(Keys.ENTER)


class SearchResultPage(BasePage):

    def go_to_next_page(self):

        """
        Goes to next page of Google search results.
        """
        print("Going to the next result page.")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*SearchResultPageLocators.NEXT_PAGE).click()

    def any_results(self):

        """
        Checks if there are any results on the page.

        :return: Boolean - True if there are more than 0 results on the page. False if there are no results.
        """
        # the below method took more time, so it's commented.
        # try:
        #     self.wait_for_element(SearchResultPageLocators.RESULTS)
        # except TimeoutException:
        #     print("There are no results.")
        #     return False
        # print("There is more than 0 results.")
        # return True

        try:
            WebDriverWait(self.driver, 5).until(
                    lambda driver: "Około 0 wyników" in driver.page_source
                )
            print("There are no results.")
            return False
        except TimeoutException:
            print("There is more than 0 results.")
            return True

    def is_page_number_matching(self, expected_number):

        """
        Checks if page number displayed is the one corresponding to the one provided in the argument.

        :param expected_number: integer
        :return: Boolean - True if the page number is corresponding to expected_number. Otherwise, False.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                    lambda driver: "Strona {} z około".format(str(expected_number)) in driver.page_source
                )
            print("Correct page number is being displayed.")
            return True
        except TimeoutException:
            return False

    def go_to_home_page(self):

        """
        Clicks the logo of Google and forwards to the homepage of Google.
        """
        print("Going to home page.")
        self.driver.find_element(*SearchResultPageLocators.HOME_PAGE).click()

    def switch_explicit_search(self):

        """
        Switches the Explicit content switch.
        """
        self.driver.find_element(*SearchResultPageLocators.SETTINGS).click()
        self.wait_for_element(SearchResultPageLocators.EXPLICIT_SWITCH).click()

    def is_safe_search_on(self):

        """
        Checks if the SafeSearch on functionality is on.

        :return: Boolean - True of the SafeSearch is on. Otherwise, False.
        """
        try:
            WebDriverWait(self.driver, 5).until(
                    lambda driver: "SafeSearch włączony" in driver.page_source
                )
            print("SafeSearch is on.")
            return True
        except TimeoutException:
            print("SafeSearch is off.")
            return False
