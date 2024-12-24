# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from auth_window_imports_options import *
from Page_Elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from Tests.test_13_Authorisation.test_13_6_1_Email_Back import email_window_check


# Создать функцию проверки возникновения ошибки "Некорректный формат почты".
def error_check():
    # Создать переменную локатора ошибки.
    TEXT_ERROR_NOT_EXIST_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Некорректный формат почты']",
    )

    # Создать переменную элемента ошибки.
    TEXT_ERROR_NOT_EXIST = driver.find_element(*TEXT_ERROR_NOT_EXIST_LOCATOR)

    # Проверить через assert, что возникла ошибка.
    assert (
        TEXT_ERROR_NOT_EXIST.text
        == "Некорректный формат почты"
    ), "Ошибка не появилась :-("

    # Проверить через print, что возникла ошибка.
    if (
        TEXT_ERROR_NOT_EXIST.text
        == "Некорректный формат почты"
    ):
        print("Ошибка появилась!")
    else:
        print("Ошибка не появилась :-(")


# Создать функцию клика на кнопку "Войти" и проверки ошибки "Некорректный формат почты".
def click_and_check():
    # Кликнуть на кнопку "Войти".
    wait.until(EC.element_to_be_clickable(email_window.LOGIN_BUTTON)).click()
    time.sleep(3)

    # Проверить возникновение ошибки.
    error_check()


# Открыть окно "Войдите по почте".
email_window_check()

# Создать объект окна "Войдите по почте"
# класса MainPageAuthorisationEmailWindow.
email_window = MainPageAuthorisationEmailWindow(driver)

# ТЕСТ 13.6.4.9
# Кликнуть на поле ввода и ввести данные.
(
    action.click(email_window.INPUT_FIELD)
    .pause(1)
    .send_keys("w w@w.ww")
    .perform()
)
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

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
