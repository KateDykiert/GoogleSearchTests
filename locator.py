from selenium.webdriver.common.by import By


class BasePageLocators(object):
    SIGN_IN_BUTTON = (By.XPATH, "//a[text()='Sign in']")


class SignInPageLocators(object):
    EMAIL_OR_PHONE_INPUT = (By.XPATH, "//*[@id='identifierId']")
    PASSWORD_INPUT = (By.NAME, "Passwd")
    NEXT_BUTTON = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button")


class HomePageLocators(object):
    SUGGESTED_LANGUAGE = (By.XPATH, "//a[parent::div[@id='SIvCob']]")
    ACCEPT_ALL_COOKIES = (By.ID, "L2AGLb")
    MAIN_SEARCH = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    GOOGLE_SEARCH = (By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")


class SearchResultPageLocators(object):
    pass
