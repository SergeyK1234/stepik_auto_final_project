import pytest
from selenium.webdriver.common.by import By

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators


PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_on_add_to_cart_button()
#     page.solve_quiz_and_get_code()
#     page.success_message_should_be_present()
#     page.title_should_be_in_success_message()
#     page.price_should_be_equal

# @pytest.mark.skip
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, PRODUCT_LINK)
#     page.open()
#     page.click_on_add_to_cart_button()
#     assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
#         'Element is present'


# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, PRODUCT_LINK)
#     page.open()
#     assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
#         'Element is present'


# @pytest.mark.skip
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, PRODUCT_LINK)
#     page.open()
#     page.click_on_add_to_cart_button()
#     assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
#         'Element is present'


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()