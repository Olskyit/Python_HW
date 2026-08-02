from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_modal_window():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/entry_ad")

        modal = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal"))
        )
        assert modal.is_displayed()

        modal_text = modal.find_element(By.CLASS_NAME, "modal-title")
        assert (
            modal_text.text.lower() == "this is a modal window"
        ), "Текст модального окна не соответствует ожидаемому"

        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Close']"))
        )
        close_btn.click()

        wait.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "modal"))
        )

        content = driver.find_element(By.ID, "content")
        assert content.is_displayed()

    finally:
        driver.quit()
