from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_multiple_elements():
    driver = webdriver.Chrome()

    try:
        driver.get("https://httpbin.org/links/10")

        # Ждём загрузки всех ссылок (должно быть ровно 9)
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(By.TAG_NAME, "a")) == 9
        )

        # Находим все ссылки на странице
        links = driver.find_elements(By.TAG_NAME, "a")

        # Проверяем, что количество ссылок равно 9
        assert len(links) == 9

        # Проверяем, что все ссылки отображаются на странице
        for link in links:
            assert link.is_displayed()

        # Проверяем, что текст первой ссылки содержит "1"
        assert "1" in links[0].text

    finally:
        driver.quit()
