from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:

    URL = (
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/"
        "slow-calculator.html"
    )

    DELAY = (By.ID, "delay")
    RESULT = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        delay = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(self.DELAY)
        )

        delay.clear()
        delay.send_keys(str(seconds))

    def click_button(self, value):
        button = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//span[text()='{value}']"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def calculate(self):
        self.click_button("7")
        self.click_button("+")
        self.click_button("8")
        self.click_button("=")

    def wait_result(self, value, timeout):
        WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.text_to_be_present_in_element(
                self.RESULT,
                value
            )
        )

    def get_result(self):
        return self.driver.find_element(
            *self.RESULT
        ).text
