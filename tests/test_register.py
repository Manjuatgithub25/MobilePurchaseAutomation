from pageobjects.Checkout_items_page import CheckoutItems
from pageobjects.Register_page import RegisterPage
from pageobjects.checkout_page import Checkout
from pageobjects.purchase_page import Purchase
from utilities.baseclass import BaseClass


class TestRegister(BaseClass):

    def test_register(self):
        logg = self.output_log()
        register_page = RegisterPage(self.driver)
        register_page.user_name()
        register_page.user_email()
        register_page.password()
        register_page.click_checkbox()
        register_page.gender_selection()
        register_page.status()
        register_page.date_of_birth()
        register_page.submit()
        assert register_page.assert_submit() == "Success!"
        logg.info(register_page.assert_submit())
        register_page.shop_page()

    def test_phone_purchase(self):
        logg = self.output_log()
        checkout_page = CheckoutItems(self.driver)
        purchasePage = Purchase(self.driver)
        checkoutItems_page = Checkout(self.driver)
        brands = checkout_page.phone_name()
        for brand in brands:
            logg.info(brand.text)
            if brand.text == "Blackberry":
                checkout_page.add_btn()

        checkout_page.checkout_item()
        checkoutItems_page.checkout()
        purchasePage.enter_country()
        purchasePage.select_country()
        purchasePage.agree()
        purchasePage.purchase()
        assert "Success!" in purchasePage.assertion_check()
        logg.info(purchasePage.assertion_check())
