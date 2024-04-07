from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def checks_the_text_that_the_cart_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET), \
            "there is a product in the cart"
        text_basket_in_empty = self.browser.find_element(*BasePageLocators.PRODUCT_BASKET_TEXT)
        assert text_basket_in_empty.text == "Your basket is empty. Continue shopping", \
            "there is no message that the cart is empty or the message is incorrect"

    def checks_that_cart_is_empty(self):
        assert self.is_disappeared(*BasePageLocators.PRODUCT_IN_BASKET), \
            "there is a product in the cart"
        text_basket_in_empty = self.browser.find_element(*BasePageLocators.PRODUCT_BASKET_TEXT)
        assert text_basket_in_empty.text == "Your basket is empty. Continue shopping", \
            "there is no message that the cart is empty or the message is incorrect"
