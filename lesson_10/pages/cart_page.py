from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    """
    Page Object страницы корзины.
    """

    CHECKOUT = (By.ID, "checkout")
    ITEMS = (By.CLASS_NAME, "inventory_item_name")

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

    def checkout(self) -> None:
        """
        Нажимает кнопку перехода к оформлению заказа.

        Returns:
            None.
        """
        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.CHECKOUT
            )
        ).click()

    def get_items(self) -> list[str]:
        """
        Получает список товаров в корзине.

        Returns:
            list[str]: список названий товаров.
        """
        items = self.driver.find_elements(
            *self.ITEMS
        )

        return [
            item.text
            for item in items
        ]
