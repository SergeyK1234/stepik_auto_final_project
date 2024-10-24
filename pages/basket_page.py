from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        items = self.browser.find_elements(
            *BasketPageLocators.PRODUCTS_IN_BASKET
        )
        assert len(items) == 0, \
            f'Basket is not empty, value = {len(items)}'

    def message_basket_empty_should_be_presented(self):
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_BASKET_IS_EMPTY
        ), \
            "Message is not presented"
