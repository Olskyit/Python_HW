import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description(
    "Проверка вычисления выражения 7 + 8 "
    "с задержкой 45 секунд"
)
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator() -> None:
    """
    Проверяет корректность работы калькулятора.

    Проверяемый сценарий:
    1. Открытие страницы калькулятора.
    2. Установка задержки 45 секунд.
    3. Выполнение операции 7 + 8.
    4. Проверка результата 15.
    """

    driver = webdriver.Chrome()

    try:
        calculator_page = CalculatorPage(driver)

        with allure.step(
            "Открыть страницу калькулятора"
        ):
            calculator_page.open()

        with allure.step(
            "Установить задержку 45 секунд"
        ):
            calculator_page.set_delay(45)

        with allure.step(
            "Выполнить вычисление 7 + 8"
        ):
            calculator_page.calculate()

        with allure.step(
            "Дождаться появления результата 15"
        ):
            calculator_page.wait_result(
                "15",
                50
            )

        with allure.step(
            "Проверить результат вычисления"
        ):
            assert calculator_page.get_result() == "15"

    finally:
        driver.quit()
