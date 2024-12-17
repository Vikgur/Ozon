# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from auth_window_imports_options import *
from Page_Elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from Tests.test_13_Authorisation.test_13_6_1_Email_Back import email_window_check


# Создать функцию проверки возникновения ошибки "Не можем найти аккаунт
# с этой почтой. Попробуйте ввести другую или войти по номеру телефона.".
def error_check():
    # Создать переменную локатора ошибки.
    TEXT_error_check_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Не можем найти аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона.']",
    )

    # Создать переменную элемента ошибки.
    TEXT_error_check = driver.find_element(*TEXT_error_check_LOCATOR)

    # Проверить через assert, что возникла ошибка.
    assert (
        TEXT_error_check.text
        == "Не можем найти аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона."
    ), "Ошибка не появилась :-("

    # Проверить через print, что возникла ошибка.
    if (
        TEXT_error_check.text
        == "Не можем найти аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона."
    ):
        print("Ошибка появилась!")
    else:
        print("Ошибка не появилась :-(")


# Создать функцию клика на кнопку "Войти" и проверки ошибки "Не можем найти
# аккаунт с этой почтой. Попробуйте ввести другую или войти по номеру телефона.".
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

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
