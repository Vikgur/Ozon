# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation import email_window_asserts


@allure.description(
    "Тесты: 13.6.4.9, 13.6.4.10, 13.6.4.11, 13.6.4.12, 13.6.4.13, 13.6.4.14, 13.6.4.15, 13.6.4.16, 13.6.4.17, 13.6.4.18"
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
# Создать функцию клика на кнопку "Войти" и проверки ошибки "Некорректный формат почты".
def click_and_check():
    # Создать объект класса EmailWindow.
    window = email_window_asserts.TestEmailWindow()

    # Создать объект окна "Войдите по почте"
    # класса MainPageAuthorisationEmailWindow.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Кликнуть на кнопку "Войти".
    wait.until(EC.element_to_be_clickable(email_window.LOGIN_BUTTON)).click()
    time.sleep(3)

    # Проверить возникновение ошибки.
    window.error_check_incorrect_format()


def test_from_9_till_18():
    # Открыть окно "Войдите по почте".
    email_window_check()

    # Создать объект окна "Войдите по почте"
    # класса MainPageAuthorisationEmailWindow.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # ТЕСТ 13.6.4.9
    # Кликнуть на поле ввода и ввести данные.
    (action.click(email_window.INPUT_FIELD).pause(1).send_keys("w w@w.ww").perform())
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.9 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.10
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("ж@w.ww")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.10 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.11
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w_-1@www")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.11 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.12
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w_-1w.ww")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.12 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.13
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.13 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.14
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w/w@w.ww")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.14 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.15
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("<div>")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.15 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.16
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("'); SELECT * FROM users; )")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.16 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.17
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("<script>alert('xss');</script>")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.17 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.18
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("123.123.123.123")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.18 ПРОЙДЕН УСПЕШНО!")

    driver.quit()
