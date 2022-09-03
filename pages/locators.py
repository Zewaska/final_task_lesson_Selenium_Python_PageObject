from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BASCET_LINK = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div > h1")
    BOOK_NAME_ALERT = (By.CSS_SELECTOR, "div[class='alertinner ']> strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div> p[class='price_color']")
    BOOK_PRICE_ALERT = (By.CSS_SELECTOR, "div[class='alertinner '] > p > strong")
