from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a:nth-child(1)')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (
        By.CSS_SELECTOR, 'button.btn-add-to-basket'
    )
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, 'div.alert:nth-child(1)')
    CART_PRICE = (
        By.CSS_SELECTOR, 'div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)'
    )
    PRODUCT_PRICE = (
        By.CSS_SELECTOR, 'p.price_color'
    )
    PRODUCT_TITLE = (
        By.CSS_SELECTOR, 'div.col-sm-6:nth-child(2) > h1:nth-child(1)'
    )
    PRODUCT_TITLE_IN_MESSAGE = (
        By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)'
    )


class BasketPageLocators():
    PRODUCTS_IN_BASKET = (
        By.CSS_SELECTOR, 'div.basket-items'
    )
    MESSAGE_BASKET_IS_EMPTY = (
        By.CSS_SELECTOR, '#content_inner > p:nth-child(1)'
    )
    MESSAGE_BASKET_IS_EMPTY = (
        By.CSS_SELECTOR, '#content_inner > p:nth-child(12)'
    )
