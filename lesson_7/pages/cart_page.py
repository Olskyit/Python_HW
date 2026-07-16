from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CHECKOUT = (By.ID, "checkout")
    ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.CHECKOUT
            )
        ).click()

    def get_items(self):

        items = self.driver.find_elements(
            *self.ITEMS
        )

        return [
            item.text
            for item in items
        ]
