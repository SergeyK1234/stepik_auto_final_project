from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def click_on_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON
        )
        add_to_cart_button.click()

    def success_message_should_be_present(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), 'Succes message is not presented'

    def title_should_be_in_success_message(self):
        product_title = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE
        )
        title_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE_IN_MESSAGE
        )
        assert product_title.text == title_in_message.text, \
            f'Wrong title, expected result: {product_title}, result {title_in_message}'

    def price_should_be_equal(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        cart_price = self.browser.find_element(
            *ProductPageLocators.CART_PRICE
        )
        assert product_price.text == cart_price.text, \
            f'Wrong value, expected result {product_price}, result {cart_price}'
