from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """
    Page Object для страницы калькулятора.
    """

    URL = (
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/"
        "slow-calculator.html"
    )

    DELAY = (By.ID, "delay")
    RESULT = (By.CLASS_NAME, "screen")

    def __init__(
        self,
        driver: WebDriver
    ) -> None:
        """
        Инициализация страницы.

        Args:
            driver (WebDriver): экземпляр Selenium WebDriver.

        Returns:
            None.
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        Returns:
            None.
        """
        self.driver.get(self.URL)

    def set_delay(
        self,
        seconds: int
    ) -> None:
        """
        Устанавливает задержку вычисления.

        Args:
            seconds (int): значение задержки в секундах.

        Returns:
            None.
        """
        delay = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.DELAY
            )
        )

        delay.clear()
        delay.send_keys(str(seconds))

    def click_button(
        self,
        value: str
    ) -> None:
        """
        Нажимает кнопку калькулятора.

        Args:
            value (str): значение кнопки.

        Returns:
            None.
        """
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

    def calculate(self) -> None:
        """
        Выполняет расчет 7 + 8.

        Returns:
            None.
        """
        self.click_button("7")
        self.click_button("+")
        self.click_button("8")
        self.click_button("=")

    def wait_result(
        self,
        value: str,
        timeout: int
    ) -> None:
        """
        Ожидает появления результата.

        Args:
            value (str): ожидаемый результат.
            timeout (int): время ожидания в секундах.

        Returns:
            None.
        """
        WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.text_to_be_present_in_element(
                self.RESULT,
                value
            )
        )

    def get_result(self) -> str:
        """
        Получает результат вычисления.

        Returns:
            str: текст результата.
        """
        return self.driver.find_element(
            *self.RESULT
        ).text
