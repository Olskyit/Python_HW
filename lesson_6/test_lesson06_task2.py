from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    try:
        # 1. Открываем сайт Gitflic
        driver.get("https://gitflic.ru/")

        # 2. Устанавливаем cookie пользователя 1 (сессия)
        driver.add_cookie({
            "name": "SESSION",
            "value": "NDkwZDE5ZjYtNzI5Yy00NjFhLWJiNDYtNGUxNGZlOTAwOTNj",
            "domain": "gitflic.ru"
        })

        # 3. Устанавливаем cookie подтверждения cookies
        driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
        })

        # 4. Обновляем страницу, чтобы применились cookies
        driver.refresh()

        # 5. Переходим в профиль пользователя 1
        driver.get("https://gitflic.ru/user/airsworld")

        # 6. Сохраняем URL пользователя 1
        url_user1 = driver.current_url

        # 7. Проверяем, что мы действительно на странице профиля 1
        assert "airsworld" in url_user1

        # 8. Разлогиниваемся (очистка cookies)
        driver.delete_all_cookies()

        # 9. Перезагружаем сайт после выхода
        driver.get("https://gitflic.ru/")

        # 10. Устанавливаем cookie пользователя 2
        driver.add_cookie({
            "name": "SESSION",
            "value": "YOUR_REAL_USER2_SESSION_ID",
            "domain": "gitflic.ru"
        })

        driver.add_cookie({
            "name": "cookiesAccepted",
            "value": "true",
            "domain": "gitflic.ru"
        })

        # 11. Обновляем страницу
        driver.refresh()

        # 12. Переходим в профиль пользователя 2
        driver.get("https://gitflic.ru/user/OTHER_USERNAME")

        # 13. Сохраняем URL пользователя 2
        url_user2 = driver.current_url

        # 14. Проверяем, что профиль действительно другой
        assert "OTHER_USERNAME" in url_user2
        assert url_user1 != url_user2

    finally:
        driver.quit()
