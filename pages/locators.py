from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    BASKET_EMPTY = (By.CSS_SELECTOR, "p > a")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div > h2")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PASSWORD = (By.NAME, "registration-password1")
    CONFIRM_REG_PASSWORD = (By.NAME, "registration-password2")
    REGISTER = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASCET_ADD_LINK = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET_LINK = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    BOOK_NAME = (By.CSS_SELECTOR, "div > h1")
    BOOK_NAME_ALERT = (By.CSS_SELECTOR, "div[class='alertinner ']> strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div> p[class='price_color']")
    BOOK_PRICE_ALERT = (By.CSS_SELECTOR, "div[class='alertinner '] > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
