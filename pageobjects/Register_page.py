from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageobjects.Checkout_items_page import CheckoutItems


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "name")
    useremail = (By.NAME, "email")
    pw = (By.CSS_SELECTOR, "input[type='password']")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    status_click = (By.XPATH, "//label[text()='Student']")
    DOB = (By.NAME, "bday")
    btn = (By.CLASS_NAME, "btn-success")
    assertion = (By.XPATH, "//div/div[2]/div/strong")
    shop_btn = (By.XPATH, "//ul/li[2]/a")

    def user_name(self):
        return self.driver.find_element(*RegisterPage.username).send_keys("Manjunath")

    def user_email(self):
        return self.driver.find_element(*RegisterPage.useremail).send_keys("v7688705@gmail.com")

    def password(self):
        return self.driver.find_element(*RegisterPage.pw).send_keys("0987654321")

    def click_checkbox(self):
        return self.driver.find_element(*RegisterPage.checkbox).click()

    def gender_selection(self):
        dropdown = Select(self.driver.find_element(*RegisterPage.gender))
        return dropdown.select_by_visible_text("Male")

    def status(self):
        return self.driver.find_element(*RegisterPage.status_click).click()

    def date_of_birth(self):
        return self.driver.find_element(*RegisterPage.DOB).send_keys("22-03-2002")

    def submit(self):
        return self.driver.find_element(*RegisterPage.btn).click()

    def assert_submit(self):
        msg = self.driver.find_element(*RegisterPage.assertion)
        return msg.text

    def shop_page(self):
        return self.driver.find_element(*RegisterPage.shop_btn).click()


