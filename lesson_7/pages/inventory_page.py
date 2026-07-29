from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self, product_name):

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

    def open_cart(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.CART
            )
        ).click()
