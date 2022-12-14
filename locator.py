from selenium.webdriver.common.by import By


class BasePageLocators(object):
    SIGN_IN_BUTTON = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div[2]/a")
    # SIGN_IN_BUTTON = (By.CLASS_NAME, "gb_1 gb_2 gb_8d gb_4 gb_8c")


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
    NEXT_PAGE = (By.XPATH, "//*[@id='pnnext']")
    HOME_PAGE = (By.XPATH, "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[1]/a/img")
    SETTINGS = (By.XPATH, "/html/body/div[4]/div[2]/div/div[1]/div/span")
    EXPLICIT_SWITCH = (By.XPATH, "/html/body/div[7]/div/div[7]/div[2]/div[2]/div[3]/div[1]/div/div[2]"
                                 "/g-selection-control-switch/label/div[2]")
    RESULTS = (By.XPATH, "//h3")
