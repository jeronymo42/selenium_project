from .pages.product_page import PromoNewYearPage
from .pages.cart_page import CartPage
from .pages.locators import PromoNewYearPageLocators

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

# def test_add_to_cart(browser):
#     page = PromoNewYearPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.solve_quiz_and_get_code()

def test_guest_can_add_product_to_basket(browser):
    page = PromoNewYearPage(browser, link)
    page.open()
    book_title = page.browser.find_element(*PromoNewYearPageLocators.BOOK_TITLE).text
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.go_to_cart()
    print(book_title)
    page = CartPage(browser=page.browser, url=page.browser.current_url)
    item_in_cart = False
    for elem in page.get_items_from_cart():
        if book_title == elem.text:
            item_in_cart = True
    assert item_in_cart, "Added book not in Cart =("
