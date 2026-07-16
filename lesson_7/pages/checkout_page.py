from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(
        self,
        first_name,
        last_name,
        postal
    ):

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

    def get_total(self):

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
