from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT_IN_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_IN_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_INPUT_IN_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_IN_REGISTER_FORM = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_TITLE_IN_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success > div > strong")
    BASKET_ALERT = (By.CSS_SELECTOR, ".alert-info")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color")
    TOTAL_IN_BASKET_ALERT = (By.CSS_SELECTOR, ".alert-info > div > p > strong")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    GOODS_BLOCK = (By.CSS_SELECTOR, "#content_inner > .basket_summary")
