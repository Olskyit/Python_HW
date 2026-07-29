from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_content():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_btn.click()

        finish_element = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        message = finish_element.text

        assert message != ""
        assert "Hello World!" in message

    finally:
        driver.quit()
