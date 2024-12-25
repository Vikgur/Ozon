# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation import email_window_asserts


# Создать функцию клика на кнопку "Войти" и проверки ошибки "Не можем найти
# аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона.".
def click_and_check():
    # Создать объект класса EmailWindow.
    window = email_window_asserts.EmailWindow()

    # Создать объект окна "Войдите по почте"
    # класса MainPageAuthorisationEmailWindow.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Кликнуть на кнопку "Войти".
    wait.until(EC.element_to_be_clickable(email_window.LOGIN_BUTTON)).click()
    time.sleep(3)

    # Проверить возникновение ошибки.
    window.error_check_empty_account()


def test_from_3_till_6():

    # Открыть окно "Войдите по почте".
    email_window_check()

    # Создать объект окна "Войдите по почте"
    # класса MainPageAuthorisationEmailWindow.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # ТЕСТ 13.6.4.3
    # Кликнуть на поле ввода и ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("w_-1@w.ww")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.3 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.4
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("W_-1@W.WW")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.4 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.5
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys(" ww@w.ww")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.5 ПРОЙДЕН УСПЕШНО!")

    # ТЕСТ 13.6.4.6
    # Ввести данные.
    (
        action.click(email_window.INPUT_FIELD)
        .double_click(email_window.INPUT_FIELD)
        .pause(1)
        .send_keys("ww@w.ww ")
        .perform()
    )
    time.sleep(1)

    # Кликнуть на "Войти" и проверить ошибку.
    click_and_check()

    print("ТЕСТ 13.6.4.6 ПРОЙДЕН УСПЕШНО!")

    driver.quit()
