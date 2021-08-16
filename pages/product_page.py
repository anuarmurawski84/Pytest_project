from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button.click()

    def guest_can_see_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART)
        assert product_name.text in product_name_in_cart.text, "Product is missing"

    def product_price_is_displayed_correctly(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART)
        assert product_price.text in product_price_in_cart.text, "Price is not correct"
