from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.login_page import LoginPage


MAIN_LINK = 'http://selenium1py.pythonanywhere.com/'
LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = MAIN_LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_form_is_exists(browser):
    page = LoginPage(browser, LOGIN_LINK)
    page.open()
    page.should_be_login_form()


def test_register_form_is_exists(browser):
    page = LoginPage(browser, LOGIN_LINK)
    page.open()
    page.should_be_register_form()
