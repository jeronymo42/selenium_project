from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.open()
        assert self.browser.current_url == self.url

    def should_be_login_form(self):
        self.open()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        self.open()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"