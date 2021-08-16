import pytest

from .pages.product_page import ProductPage
import time

@pytest.mark.parametrize('url_parameter', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                  "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                  "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                    "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, url_parameter):
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{url_parameter}"

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.guest_can_add_to_cart()
    product_page.solve_quiz_and_get_code()
    time.sleep(3)
    product_page.guest_can_see_product_name()
    time.sleep(3)
    product_page.product_price_is_displayed_correctly()