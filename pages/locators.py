from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form.well")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    ADDED_MESSAGE = (By.CLASS_NAME, "alertinner strong")
    NAME_PRODUCT = (By.CLASS_NAME, 'col-sm-6.product_main h1')
    ADDED_COST_MESSAGE = (By.CLASS_NAME, "alertinner p strong")
    COST_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success")
