import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time


@pytest.mark.new_class
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@companymail.com"
        password = str(time.time())
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.register_new_user(email, password, browser)
        self.login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.guest_can_add_to_cart()
        product_page.guest_can_see_product_name()
        time.sleep(3)
        product_page.product_price_is_displayed_correctly()



@pytest.mark.xfail(reason="guest can see success message after adding product to cart")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.guest_can_add_to_cart()
    product_page.solve_quiz_and_get_code()
    time.sleep(5)
    product_page.should_be_message_about_adding_to_cart()



@pytest.mark.xfail(reason="success message is not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.guest_can_add_to_cart()
    product_page.should_success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.go_to_login_page()
    login_page.should_be_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.guest_can_go_to_basket_page()
    basket_page.guest_cant_see_product_in_basket()
    basket_page.guest_can_see_empty_basket()

# @pytest.mark.parametrize('url_parameter', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
#                                   "?promo=offer3", "?promo=offer4", "?promo=offer5",
#                                   "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail),
#                                     "?promo=offer8", "?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, url_parameter):
#     # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{url_parameter}"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.guest_can_add_to_cart()
#     product_page.solve_quiz_and_get_code()
#     time.sleep(3)
#     product_page.guest_can_see_product_name()
#     time.sleep(3)
#     product_page.product_price_is_displayed_correctly()
