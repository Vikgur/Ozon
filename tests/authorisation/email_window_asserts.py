# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check


class EmailWindow:

    # Создать функцию проверки возникновения ошибки "Не можем найти аккаунт
    # с этой почтой. Попробуйте ввести другую или войти по номеру телефона.".
    def error_check_empty_account(self):
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

    # Создать функцию проверки возникновения ошибки "Заполните почту".
    def error_check_fill_email(self):
        # Создать переменную локатора ошибки.
        TEXT_ERROR_NOT_EXIST_LOCATOR = (
            "xpath",
            "//div[normalize-space(.)='Заполните почту']",
        )

        # Создать переменную элемента ошибки.
        TEXT_ERROR_NOT_EXIST = driver.find_element(*TEXT_ERROR_NOT_EXIST_LOCATOR)

        # Проверить через assert, что возникла ошибка.
        assert TEXT_ERROR_NOT_EXIST.text == "Заполните почту", "Ошибка не появилась :-("

        # Проверить через print, что возникла ошибка.
        if TEXT_ERROR_NOT_EXIST.text == "Заполните почту":
            print("Ошибка появилась!")
        else:
            print("Ошибка не появилась :-(")

    # Создать функцию проверки возникновения ошибки "Некорректный формат почты".
    def error_check_incorrect_format(self):
        # Создать переменную локатора ошибки.
        TEXT_ERROR_NOT_EXIST_LOCATOR = (
            "xpath",
            "//div[normalize-space(.)='Некорректный формат почты']",
        )

        # Создать переменную элемента ошибки.
        TEXT_ERROR_NOT_EXIST = driver.find_element(*TEXT_ERROR_NOT_EXIST_LOCATOR)

        # Проверить через assert, что возникла ошибка.
        assert (
            TEXT_ERROR_NOT_EXIST.text == "Некорректный формат почты"
        ), "Ошибка не появилась :-("

        # Проверить через print, что возникла ошибка.
        if TEXT_ERROR_NOT_EXIST.text == "Некорректный формат почты":
            print("Ошибка появилась!")
        else:
            print("Ошибка не появилась :-(")
