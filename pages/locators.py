from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE = (By.TAG_NAME, "h1")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_TITLE_IN_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success > div > strong")
    BASKET_ALERT = (By.CSS_SELECTOR, ".alert-info")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main > .price_color")
    TOTAL_IN_BASKET_ALERT = (By.CSS_SELECTOR, ".alert-info > div > p > strong")
