from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """
    Page Object страницы авторизации.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

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
        Открывает страницу авторизации.

        Returns:
            None.
        """
        self.driver.get(self.URL)

    def login(
        self,
        username: str,
        password: str
    ) -> None:
        """
        Выполняет авторизацию пользователя.

        Args:
            username (str): логин пользователя.
            password (str): пароль пользователя.

        Returns:
            None.
        """
        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.USERNAME
            )
        ).send_keys(username)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        self.driver.find_element(
            *self.LOGIN
        ).click()
