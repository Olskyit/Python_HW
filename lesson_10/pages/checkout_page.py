from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    """
    Page Object страницы оформления заказа.
    """

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

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

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal: str
    ) -> None:
        """
        Заполняет форму оформления заказа.

        Args:
            first_name (str): имя покупателя.
            last_name (str): фамилия покупателя.
            postal (str): почтовый индекс.

        Returns:
            None.
        """
        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        ).send_keys(first_name)

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *self.POSTAL
        ).send_keys(postal)

        self.driver.find_element(
            *self.CONTINUE
        ).click()

    def get_total(self) -> str:
        """
        Получает итоговую стоимость заказа.

        Returns:
            str: итоговая сумма заказа.
        """
        total = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.TOTAL
            )
        )

        return total.text.replace(
            "Total: ",
            ""
        )
