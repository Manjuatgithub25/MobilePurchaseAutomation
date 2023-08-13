from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    checkoutBtn = (By.XPATH, "//button[@class='btn btn-success']")

    def checkout(self):
        return self.driver.find_element(*Checkout.checkoutBtn).click()
