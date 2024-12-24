# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.test_13_authorisation.test_13_6_1_email_back import email_window_check


# Создать функцию проверки возникновения ошибки "Заполните почту".
def error_check():
    # Создать переменную локатора ошибки.
    TEXT_ERROR_NOT_EXIST_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Заполните почту']",
    )

    # Создать переменную элемента ошибки.
    TEXT_ERROR_NOT_EXIST = driver.find_element(*TEXT_ERROR_NOT_EXIST_LOCATOR)

    # Проверить через assert, что возникла ошибка.
    assert (
        TEXT_ERROR_NOT_EXIST.text
        == "Заполните почту"
    ), "Ошибка не появилась :-("

    # Проверить через print, что возникла ошибка.
    if (
        TEXT_ERROR_NOT_EXIST.text
        == "Заполните почту"
    ):
        print("Ошибка появилась!")
    else:
        print("Ошибка не появилась :-(")


# Создать функцию клика на кнопку "Войти" и проверки ошибки "Заполните почту".
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

# ТЕСТ 13.6.4.7
# Кликнуть на поле ввода и ввести данные.
(
    action.click(email_window.INPUT_FIELD)
    .pause(1)
    .send_keys(" ")
    .perform()
)
time.sleep(1)

# Кликнуть на "Войти" и проверить ошибку.
click_and_check()

print("ТЕСТ 13.6.4.7 ПРОЙДЕН УСПЕШНО!")

# ТЕСТ 13.6.4.8
# Ввести данные.
(
    action.click(email_window.INPUT_FIELD)
    .double_click(email_window.INPUT_FIELD)
    .pause(1)
    .send_keys(Keys.BACKSPACE)
    .pause(1)
    .send_keys("")
    .perform()
)
time.sleep(1)

# Кликнуть на "Войти" и проверить ошибку.
click_and_check()

print("ТЕСТ 13.6.4.8 ПРОЙДЕН УСПЕШНО!")

driver.quit()

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
