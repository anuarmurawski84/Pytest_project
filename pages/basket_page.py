from .locators import BasePageLocators, BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def guest_can_go_to_basket_page(self):
        button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        button.click()

    def guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_IN_BASKET), "Product in basket is presented, but it should not be"

    def guest_can_see_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)