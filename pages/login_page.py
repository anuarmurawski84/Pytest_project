import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password, browser):
        registration_email = browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(email)
        time.sleep(2)
        registration_password = browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_password.send_keys(password)
        time.sleep(2)
        registration_password_repeat = browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        registration_password_repeat.send_keys(password)
        time.sleep(2)
        registration_button = browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
        time.sleep(4)


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # подстрока "login" есть в текущем url браузера
        assert "login" in self.browser.current_url, "'login' not in current url"


    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"