from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    try:
        # Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(
            By.ID,
            "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID,
            "login-button"
        ).click()

        # Ждем загрузки страницы товаров
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        # Добавляем товары в корзину
        driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        ).click()

        driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

        driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-onesie"
        ).click()

        # Переходим в корзину
        driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()

        # Нажимаем Checkout
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()

        # Заполняем данные покупателя
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        ).send_keys("Иван")

        driver.find_element(
            By.ID,
            "last-name"
        ).send_keys("Петров")

        driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys("123456")

        # Continue
        driver.find_element(
            By.ID,
            "continue"
        ).click()

        # Получаем итоговую сумму
        total = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        ).text

        # Проверяем сумму
        assert total == "Total: $58.29"

    finally:
        driver.quit()
