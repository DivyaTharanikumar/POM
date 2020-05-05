from POM.Locators import *


class BasePageElements():
    def __init__(self, driver):
        self.driver = driver

    def search_text_element(self):
        return self.driver.find_element(*BasePageLocators.search_box)

    def click_login_link(self):
        self.driver.find_element(*BasePageLocators.login).click()


class LoginPageElements():
    def __init__(self, driver):
        self.driver = driver

    def username(self):
        return self.driver.find_element(*LoginPageLocators.username_textbox)

    def password(self):
        return self.driver.find_element(*LoginPageLocators.password_textbox)

    def signin(self):
        return self.driver.find_element(*LoginPageLocators.signin_button)


class SearchResultsPageElements():
    pass


class UserPageElements():
    pass


