from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import PromoNewYearPageLocators
import math

class PromoNewYearPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*PromoNewYearPageLocators.ADD_TO_CART)
        add_button.click()


    def go_to_cart(self):
        go_to_cart_button = self.browser.find_element(*PromoNewYearPageLocators.CHECK_CART)
        go_to_cart_button.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # try:
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")
