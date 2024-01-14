from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        # self.solve_quiz_and_get_code()

    def should_correct_item_title_in_success_alert(self):
        item_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        item_title_in_success_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_IN_SUCCESS_ALERT).text
        assert item_title == item_title_in_success_alert, "Item title in success alert doesn't equal to main item title"

    def should_correct_basket_total(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.TOTAL_IN_BASKET_ALERT).text
        assert item_price == basket_total, "Basket total doesn't equal to item price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "Success message doesn't disappear"