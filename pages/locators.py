from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CLASS_NAME, "btn-group")
    PRODUCT_IN_BASKET = (By.CLASS_NAME, "basket-items")
    PRODUCT_BASKET_TEXT = (By.ID, 'content_inner')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form.well")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    REGISTER_ADD_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_ADD_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    BUTTON_REGISTER = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    ADDED_MESSAGE = (By.CLASS_NAME, "alertinner strong")
    NAME_PRODUCT = (By.CLASS_NAME, 'col-sm-6.product_main h1')
    ADDED_COST_MESSAGE = (By.CLASS_NAME, "alertinner p strong")
    COST_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success")
