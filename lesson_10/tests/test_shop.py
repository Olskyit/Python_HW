import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.title(
    "Проверка оформления заказа в магазине"
)
@allure.description(
    "Авторизация, добавление товаров "
    "и проверка итоговой стоимости"
)
@allure.feature("Shop")
@allure.severity(
    allure.severity_level.CRITICAL
)
def test_shop() -> None:
    """
    Проверяет оформление заказа.
    """

    options = Options()

    options.binary_location = (
        r"C:\Program Files\Mozilla Firefox\firefox.exe"
    )

    driver = webdriver.Firefox(
        options=options
    )

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step(
            "Открыть магазин"
        ):
            login_page.open()

        with allure.step(
            "Авторизоваться пользователем standard_user"
        ):
            login_page.login(
                "standard_user",
                "secret_sauce"
            )

        with allure.step(
            "Добавить товары в корзину"
        ):
            inventory_page.add_product(
                "Sauce Labs Backpack"
            )

            inventory_page.add_product(
                "Sauce Labs Bolt T-Shirt"
            )

            inventory_page.add_product(
                "Sauce Labs Onesie"
            )

        with allure.step(
            "Перейти в корзину"
        ):
            inventory_page.open_cart()

        with allure.step(
            "Проверить товары"
        ):
            assert cart_page.get_items() == [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ]

        with allure.step(
            "Перейти к оформлению заказа"
        ):
            cart_page.checkout()

        with allure.step(
            "Заполнить данные покупателя"
        ):
            checkout_page.fill_form(
                "Иван",
                "Иванов",
                "123456"
            )

        with allure.step(
            "Проверить итоговую стоимость"
        ):
            assert checkout_page.get_total() == "$58.29"

    finally:
        driver.quit()
