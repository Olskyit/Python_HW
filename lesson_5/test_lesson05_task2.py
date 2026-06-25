from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_form_submission():
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.org/forms/post")

        # Даём странице время на загрузку
        time.sleep(2)

        # Находим поле по атрибуту name="custname" и вводим текст
        driver.find_element(By.NAME, "custname").send_keys("Olga")

        # Находим поле по атрибуту name="custtel" и вводим текст
        driver.find_element(By.NAME, "custtel").send_keys("1234567890")

        # Находим поле по атрибуту name="custemail" и вводим текст
        driver.find_element(By.NAME, "custemail").send_keys("test@test.com")

        # Находим кнопку с текстом "Submit" используя XPATH
        submit_btn = driver.find_element(
            By.XPATH,
            "//button[text()='Submit order']"
        )
        submit_btn.click()

        # Даём время на обработку формы
        time.sleep(1)

        # Проверяем, что URL изменился
        assert driver.current_url != "https://httpbin.org/forms/post"
        assert driver.current_url.endswith("/post")

    finally:
        driver.quit()
