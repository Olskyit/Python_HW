from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    try:
        # Открываем страницу калькулятора
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/"
            "slow-calculator.html"
        )

        driver.get(url)

        # Устанавливаем задержку 45 секунд
        delay = wait.until(
            EC.visibility_of_element_located((By.ID, "delay"))
        )

        delay.clear()
        delay.send_keys("45")

        # Выполняем расчет 7 + 8 =
        buttons = ["7", "+", "8", "="]

        for button_value in buttons:
            button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//span[text()='{button_value}']")
                )
            )

            driver.execute_script(
                "arguments[0].click();",
                button
            )

        # Ждем появления результата 15
        result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"),
                "15"
            )
        )

        # Проверяем результат вычисления
        assert result is True

    finally:
        driver.quit()
