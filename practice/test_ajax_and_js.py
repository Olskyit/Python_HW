from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ajax_content():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_controls")

        # нажимаем кнопку
        button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example button"))
        )
        button.click()

        # ждём сообщение
        message = wait.until(
            EC.visibility_of_element_located((By.ID, "message"))
        )

        assert (
            message.text != ""
        ), "Сообщение не появилось"

    finally:
        driver.quit()
