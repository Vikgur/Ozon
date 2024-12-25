# Класс проверок поля введения номера телефона.

from tests.authorisation.test_auth_window_imports_options import *


class Validate:

    # Функция проверки валидного символа в окне ввода номера телефона.
    def valid_input(self):

        # Создать переменную наличия элемента для проверки.
        PHONE_INPUT_CHECK = driver.find_elements(
            *MainPageAuthorisationWindowLocators.PHONE_INPUT_CHECK_LOCATOR
        )

        # Проверить через assert.
        assert (
            len(PHONE_INPUT_CHECK) == 0
        ), "Введены недопустимые символы в поле номера телефона :-("

        # Проверить через print.
        if len(PHONE_INPUT_CHECK) == 0:
            print("Введены допустимые символы в поле номера телефона!")
        else:
            print("Введены недопустимые символы в поле номера телефона :-(")

    # Функция проверки отсутствия символов в окне ввода номера телефона.
    def valid_empty_input(self):

        # Создать переменную наличия элемента для проверки.
        PHONE_INPUT_CHECK = driver.find_elements(
            *MainPageAuthorisationWindowLocators.PHONE_INPUT_CHECK_LOCATOR
        )

        # Проверить через assert.
        assert (
            len(PHONE_INPUT_CHECK) > 0
        ), "Введены допустимые символы в поле номера телефона :-("

        # Проверить через print.
        if len(PHONE_INPUT_CHECK) > 0:
            print("Символы в поле номера телефона отсутствуют!")
        else:
            print("Введены допустимые символы в поле номера телефона :-(")

    # Функция проверки ошибки «Некорректный формат телефона»
    # в окне ввода номера телефона.
    def valid_error_input(self):

        # Создать переменную локатора для проверки.
        ERROR_CHECK_LOCATOR = (
            "xpath",
            "//p[normalize-space(.)='Некорректный формат телефона']",
        )

        # Создать переменную наличия элемента для проверки.
        ERROR_CHECK = driver.find_elements(*ERROR_CHECK_LOCATOR)

        # Проверить через assert.
        assert (
            len(ERROR_CHECK) > 0
        ), "Введены допустимые символы в поле номера телефона :-("

        # Проверить через print.
        if len(ERROR_CHECK) > 0:
            print('Ошибка "Некорректный формат телефона" появилась!')
        else:
            print("Введены допустимые символы в поле номера телефона :-(")

    # Функция для проверки открытия окна ожидания
    # введения отправленного смс кода.
    def sms_window_open(self):

        # Создать переменные локаторов для проверки.
        SMS_CODE_CHECK_LOCATOR_1 = ("xpath", "//span[normalize-space(.)='Введите код']")
        SMS_CODE_CHECK_LOCATOR_2 = (
            "xpath",
            "//span[normalize-space(.)='Превышено количество попыток ввода']",
        )

        # Создать переменные наличия элементов для проверки.
        SMS_CODE_CHECK_1 = driver.find_elements(*SMS_CODE_CHECK_LOCATOR_1)
        SMS_CODE_CHECK_2 = driver.find_elements(*SMS_CODE_CHECK_LOCATOR_2)

        # Проверить через assert.
        assert (
            len(SMS_CODE_CHECK_1) > 0 or len(SMS_CODE_CHECK_2) > 0
        ), "Окно ожидания смс кода не открыто :-("

        # Проверить через print.
        if len(SMS_CODE_CHECK_1) > 0 or len(SMS_CODE_CHECK_2) > 0:
            print("Окно ожидания смс кода открыто: ТЕСТ ВЫПОЛНЕН УСПЕШНО!")
        else:
            print("Окно ожидания смс кода не открыто :-(")

    # Функция для проверки неоткрытия окна ожидания
    # введения отправленного смс кода.
    def sms_window_not_open(self):

        # Создать переменные локаторов для проверки.
        SMS_CODE_CHECK_LOCATOR_1 = ("xpath", "//span[normalize-space(.)='Введите код']")
        SMS_CODE_CHECK_LOCATOR_2 = (
            "xpath",
            "//span[normalize-space(.)='Превышено количество попыток ввода']",
        )

        # Создать переменные наличия элементов для проверки.
        SMS_CODE_CHECK_1 = driver.find_elements(*SMS_CODE_CHECK_LOCATOR_1)
        SMS_CODE_CHECK_2 = driver.find_elements(*SMS_CODE_CHECK_LOCATOR_2)

        # Проверить через assert.
        assert (
            len(SMS_CODE_CHECK_1) == 0 or len(SMS_CODE_CHECK_2) == 0
        ), "Окно ожидания смс кода открыто :-("

        # Проверить через print.
        if len(SMS_CODE_CHECK_1) == 0 or len(SMS_CODE_CHECK_2) == 0:
            print("Окно ожидания смс кода не открыто: ТЕСТ ВЫПОЛНЕН УСПЕШНО!")
        else:
            print("Окно ожидания смс кода открыто :-(")
