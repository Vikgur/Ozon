# Страница авторизации.

from locators.locators import AuthorisationPageLocators


class AuthorisationPage(object):

    # Кнопка "войти по почте"
    def __init__(self, driver):
        self.driver = driver
        # Текст 1 шага "Авторизация" в шапке.
        self.EMAIL_SIGN_IN = driver.find_element(
            *AuthorisationPageLocators.EMAIL_SIGN_IN_LOCATOR
        )

    # Текст "Введите номер телефона"
    def __init__(self, driver):
        self.driver = driver
        # Текст 1 шага "Авторизация" в шапке.
        self.VISIBILITY_TEXT_PHONE = driver.find_element(
            *AuthorisationPageLocators.VISIBILITY_TEXT_PHONE_LOCATOR
        )
