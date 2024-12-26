# Окно авторизации.

from locators.locators import MainPageAuthorisationEmailWindowLocators


class MainPageAuthorisationEmailWindow(object):

    def __init__(self, driver):
        # Текст "Войдите по почте".
        self.EMAIL_WINDOW = driver.find_element(
            *MainPageAuthorisationEmailWindowLocators.EMAIL_WINDOW_LOCATOR
        )
        # Кнопка "Вернуться на главный экран".
        self.BACK_TO_AUTHORISATION_WINDOW = driver.find_element(
            *MainPageAuthorisationEmailWindowLocators.BACK_TO_AUTHORISATION_WINDOW_LOCATOR
        )
        # Поле ввода.
        self.INPUT_FIELD = driver.find_element(
            *MainPageAuthorisationEmailWindowLocators.INPUT_FIELD_LOCATOR
        )
        # Кнопка "Войти".
        self.LOGIN_BUTTON = driver.find_element(
            *MainPageAuthorisationEmailWindowLocators.LOGIN_BUTTON_LOCATOR
        )

    def getEmailWindow(self):
        return self.EMAIL_WINDOW
