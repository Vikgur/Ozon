# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_13_6_1_email_back import email_window_check

# Открыть окно "Войдите по почте".
email_window_check()

# Создать объект окна "Войдите по почте"
# класса MainPageAuthorisationEmailWindow.
email_window = MainPageAuthorisationEmailWindow(driver)

# Кликнуть на поле ввода и ввести данные.
(
    action.click(email_window.INPUT_FIELD)
    .pause(1)
    .send_keys("viktorgurko@gmail.com")
    .perform()
)
time.sleep(2)

# Кликнуть на кнопку "Войти".
wait.until(EC.element_to_be_clickable(email_window.LOGIN_BUTTON)).click()
time.sleep(3)

# БЛОК проверок перехода на окно отправки кода.
# Если открылось окно с отправленным смс-кодом.
try:
    # Создать переменные локатора перехода на окно "Введите код".
    TEXT_ENTER_CODE_LOCATOR = ("xpath", "//span[normalize-space(.)='Введите код']")

    # Создать переменную элемента перехода на окно "Введите код".
    TEXT_ENTER_CODE = driver.find_element(*TEXT_ENTER_CODE_LOCATOR)

    # Проверить через assert, что окно "Войдите по почте" открылось.
    assert (
        TEXT_ENTER_CODE.text == "Введите код"
    ), 'Переход на окно "Введите код" не произошел :-('

    # Проверить через print, что окно "Войдите по почте" открылось.
    if TEXT_ENTER_CODE.text == "Введите код":
        print('Переход на окно "Введите код" произошел!')
    else:
        print('Переход на окно "Введите код" не произошел :-(')

# Если отправлен пуш или превышено количество попыток.
except:
    # Отправлен пуш.
    try:
        # Создать переменную локатора перехода на окно "Введите код".
        TEXT_ENTER_PUSH_CODE_LOCATOR = (
            "xpath",
            "//span[normalize-space(.)='Введите код из пуш-уведомления']",
        )

        # Создать переменную элемента перехода на окно "Введите код".
        TEXT_ENTER_PUSH_CODE = driver.find_element(*TEXT_ENTER_PUSH_CODE_LOCATOR)

        # Проверить через assert, что окно "Войдите по почте" открылось.
        assert (
            TEXT_ENTER_PUSH_CODE.text == "Введите код из пуш-уведомления"
        ), 'Переход на окно "Введите код" не произошел :-('

        # Проверить через print, что окно "Войдите по почте" открылось.
        if TEXT_ENTER_PUSH_CODE.text == "Введите код из пуш-уведомления":
            print('Переход на окно "Введите код" произошел!')
        else:
            print('Переход на окно "Введите код" не произошел :-(')         
    # Превышено количество попыток.
    except:
        # Создать переменную локатора перехода на окно "Введите код".
        TEXT_TRY_LIMIT_LOCATOR = (
            "xpath",
            "//span[normalize-space(.)='Превышено количество попыток ввода']",
        )

        # Создать переменную элемента перехода на окно "Введите код".
        TEXT_TRY_LIMIT = driver.find_element(*TEXT_TRY_LIMIT_LOCATOR)

        # Проверить через assert, что окно "Войдите по почте" открылось.
        assert (
            TEXT_TRY_LIMIT.text == "Превышено количество попыток ввода"
        ), 'Переход на окно "Введите код" не произошел :-('

        # Проверить через print, что окно "Войдите по почте" открылось.
        if TEXT_TRY_LIMIT.text == "Превышено количество попыток ввода":
            print('Переход на окно "Введите код" произошел!')
        else:
            print('Переход на окно "Введите код" не произошел :-(')

print("ТЕСТ ПРОЙДЕН УCПЕШНО!")

driver.quit()
