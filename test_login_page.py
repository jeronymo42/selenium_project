from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage

link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_login_page(browser):
    page = LoginPage(browser, link)
    page.should_be_login_page()

