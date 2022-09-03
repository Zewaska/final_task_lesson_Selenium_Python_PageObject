from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_price_and_name_book_after_buy(self):
        self.should_be_dress_name()
        self.should_be_dress_price()

    def should_be_promo_in_url(self):
        assert "?promo=newYear" in self.browser.current_url, "word \"?promo=newYear\" not in url"
    
    def should_be_add_book_in_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASCET_ADD_LINK)
        link.click()

    def should_be_add_bascet_button(self):
        assert self.is_element_present(*ProductPageLocators.BASCET_ADD_LINK), "Bascet form is not presented"        

    def should_be_dress_name(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME_ALERT).text, "Another Book Name"
        
    def should_be_dress_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ALERT).text, "Another Price Name"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message not is disappeared, but should be"

    def go_to_basket_page(self):
        self.link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        self.link.click()