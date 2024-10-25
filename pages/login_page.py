from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Not current url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), 'Register form is not presented'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(
            *LoginPageLocators.REGISTERATION_EMAIL_FIELD
        )
        email_input.send_keys(email)
        password_1_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_FIELD_1
        )
        password_1_input.send_keys(password)
        password_2_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_FIELD_2
        )
        password_2_input.send_keys(password)
        registration_submit_button = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_SUBMIT_BUTTON
        )
        registration_submit_button.click()
