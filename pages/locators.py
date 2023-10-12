from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_PAGE = '/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class PromoNewYearPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CHECK_CART = (By.CSS_SELECTOR, ".btn-group a")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")

class CartPageLocators():
    ITEMS_IN_CART = (By.CSS_SELECTOR, ".basket-items h3 a")