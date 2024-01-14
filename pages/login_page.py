from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL doesn't contain 'login' string"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_IN_REGISTER_FORM)
        email_input.send_keys(email)
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_IN_REGISTER_FORM)
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT_IN_REGISTER_FORM)
        password2_input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.SUBMIT_IN_REGISTER_FORM)
        button.click()
