from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def get_items_from_cart(self):
        items = self.browser.find_elements(*CartPageLocators.ITEMS_IN_CART)
        return items
