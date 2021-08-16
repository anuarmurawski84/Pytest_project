from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.guest_can_add_to_cart()
    product_page.solve_quiz_and_get_code()
    time.sleep(5)
    product_page.guest_can_see_product_name()
    time.sleep(5)
    product_page.product_price_is_displayed_correctly()