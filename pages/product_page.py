from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_basket.click()

    def check_product_added(self):
        added_message = self.browser.find_element(*ProductPageLocators.ADDED_MESSAGE)
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert name_product.text == added_message.text, "the product name is not the same"

    def check_cost_product_added(self):
        cost_product = self.browser.find_element(*ProductPageLocators.COST_PRODUCT)
        added_cost_message = self.browser.find_element(*ProductPageLocators.ADDED_COST_MESSAGE)
        assert cost_product.text == added_cost_message.text, "the price does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message element has not disappeared, but should not be"

