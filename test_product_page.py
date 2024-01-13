from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_element_present(*ProductPageLocators.SUCCESS_ALERT)
    page.should_correct_item_title_in_success_alert()
    page.is_element_present(*ProductPageLocators.BASKET_ALERT)
    page.should_correct_basket_total()
