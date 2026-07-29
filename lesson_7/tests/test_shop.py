from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop():

    driver = webdriver.Firefox()

    try:

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()

        login_page.login(
            "standard_user",
            "secret_sauce"
        )

        inventory_page.add_product(
            "Sauce Labs Backpack"
        )

        inventory_page.add_product(
            "Sauce Labs Bolt T-Shirt"
        )

        inventory_page.add_product(
            "Sauce Labs Onesie"
        )

        inventory_page.open_cart()

        assert cart_page.get_items() == [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        cart_page.checkout()

        checkout_page.fill_form(
            "Иван",
            "Иванов",
            "123456"
        )

        assert checkout_page.get_total() == "$58.29"

    finally:

        driver.quit()
