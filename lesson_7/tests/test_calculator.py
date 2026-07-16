from selenium import webdriver

from pages.calculator_page import CalculatorPage


def test_calculator():

    driver = webdriver.Chrome()

    try:

        calculator = CalculatorPage(driver)

        calculator.open()

        calculator.set_delay(45)

        calculator.calculate()

        calculator.wait_result(
            "15",
            50
        )

        assert calculator.get_result() == "15"

    finally:

        driver.quit()
