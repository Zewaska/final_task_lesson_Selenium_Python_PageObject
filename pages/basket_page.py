from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def go_to_basket_page(self):
        self.link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        self.link.click()
    
    def should_be_basket_form(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_LINK
            ), "Basket is not presented"
    
    def should_be_empty_basket_message(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Be Items to bascet"