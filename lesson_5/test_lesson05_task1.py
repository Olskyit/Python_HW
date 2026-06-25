from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_navigation():
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.org/")

        # Даём странице время на загрузку
        time.sleep(2)

        # Находим ссылку с href="/forms/post"
        driver.find_element(By.XPATH, "//a[@href='/forms/post']").click()

        # Проверяем смену URL на /forms/post
        assert driver.current_url.endswith("/forms/post")

        # Возвращаемся на главную страницу
        driver.back()

        # Проверяем исходный URL
        assert driver.current_url == "https://httpbin.org/"

    finally:
        driver.quit()
