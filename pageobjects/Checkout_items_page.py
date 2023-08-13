from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutItems:

    def __init__(self, driver):
        self.driver = driver

    phone_brands = (By.CSS_SELECTOR, ".card-title a")
    btn = (By.CSS_SELECTOR, ".card-footer button i")
    checkoutitem_btn = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def phone_name(self):
        return self.driver.find_elements(*CheckoutItems.phone_brands)

    def add_btn(self):
        return self.driver.find_element(*CheckoutItems.btn).click()

    def checkout_item(self):
        return self.driver.find_element(*CheckoutItems.checkoutitem_btn).click()


