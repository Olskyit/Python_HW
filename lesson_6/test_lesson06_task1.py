import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1. Создаём папку для скриншотов
        screenshots_dir = "lesson_6/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        # 2. Открываем страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 3. Нажимаем кнопку Start
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        )
        start_button.click()

        # 4. Ждём появления текста
        hello_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        WebDriverWait(driver, 10).until(
            lambda d: hello_element.text.strip() == "Hello World!"
        )

        # 5. Путь к файлу
        filename = "hello_world.png"
        root_path = filename
        final_path = os.path.join(screenshots_dir, filename)

        # 6. Делаем скриншот в корень
        driver.save_screenshot(root_path)

        # 7. Перемещаем файл в папку screenshots
        if os.path.exists(root_path):
            shutil.move(root_path, final_path)

        # 8. Проверка
        assert hello_element.text.strip() == "Hello World!"

    finally:
        driver.quit()
