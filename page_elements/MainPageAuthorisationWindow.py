# Окно авторизации.

from locators.locators import MainPageAuthorisationWindowLocators


class MainPageAuthorisationWindow(object):

    def __init__(self, driver):
        # Выпадающийц список кодов стран.
        self.CODE_LIST = driver.find_element(
            *MainPageAuthorisationWindowLocators.CODE_LIST_LOCATOR
        )
        # Поле ввода номера телефона.
        self.PHONE_INPUT_FIELD = driver.find_element(
            *MainPageAuthorisationWindowLocators.PHONE_INPUT_FIELD_LOCATOR
        )
        # Кнопка "Войти".
        self.LOGIN_BUTTON = driver.find_element(
            *MainPageAuthorisationWindowLocators.LOGIN_BUTTON_LOCATOR
        )
        # Проверка наличия пустого поля ввода номера телефона.
        self.PHONE_INPUT_CHECK = driver.find_element(
            *MainPageAuthorisationWindowLocators.PHONE_INPUT_CHECK_LOCATOR
        )
        # Кнопка "Вход через Госуслуги".
        self.GOSUSLUGI_BUTTON = driver.find_element(
            *MainPageAuthorisationWindowLocators.GOSUSLUGI_BUTTON_LOCATOR
        )
        # Кнопка "Не могу войти".
        self.CAN_NOT_SIGN_IN = driver.find_element(
            *MainPageAuthorisationWindowLocators.CAN_NOT_SIGN_IN_LOCATOR
        )
        # Кнопка "Войти по почте".
        self.EMAIL_SIGN_IN = driver.find_element(
            *MainPageAuthorisationWindowLocators.EMAIL_SIGN_IN_LOCATOR
        )

    def getCodeList(self):
        return self.CODE_LIST

    def getPhoneInputField(self):
        return self.PHONE_INPUT_FIELD
