from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators:
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button.btn-add-to-basket")