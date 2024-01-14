from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_BLOCK), \
            "Products are displayed in the basket, an empty basket is expected"

    def should_be_empty_basket_text(self):
        basket_empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        assert basket_empty_message == "Your basket is empty. Continue shopping", "Basket isn't empty"
