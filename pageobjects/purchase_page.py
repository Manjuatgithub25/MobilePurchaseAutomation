from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Purchase:

    def __init__(self, driver):
        self.driver = driver

    Enter = (By.ID, "country")
    select = (By.LINK_TEXT, "India")
    agree_click = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchase_btn = (By.XPATH, "//input[@value='Purchase']")
    assertion = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def enter_country(self):
        return self.driver.find_element(*Purchase.Enter).send_keys("ind")

    def select_country(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.presence_of_element_located((Purchase.select))).click()

    def agree(self):
        return self.driver.find_element(*Purchase.agree_click).click()

    def purchase(self):
        return self.driver.find_element(*Purchase.purchase_btn).click()

    def assertion_check(self):
        return self.driver.find_element(*Purchase.assertion).text
