from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    """
    Page Object главной страницы магазина.
    """

    CART = (By.CLASS_NAME, "shopping_cart_link")

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

    def add_product(
        self,
        product_name: str
    ) -> None:
        """
        Добавляет товар в корзину.

        Args:
            product_name (str): название товара.

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
                    f"//div[text()='{product_name}']"
                    "/ancestor::div[contains("
                    "@class,'inventory_item')]"
                    "//button"
                )
            )
        )

        button.click()

    def open_cart(self) -> None:
        """
        Переходит в корзину.

        Returns:
            None.
        """
        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.CART
            )
        ).click()
