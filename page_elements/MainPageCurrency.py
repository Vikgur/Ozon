# Модальное неблокирующее окно "Валюта".

from locators.locators import MainPageCurrencyLocators


class MainPageСurrency(object):

    def __init__(self, driver):
        # Текст "Валюта".
        self.MAIN_CURRENCY_VISIBILITY = driver.find_element(
            *MainPageCurrencyLocators.MAIN_CURRENCY_VISIBILITY_LOCATOR
        )
        # Выпадающий список валют.
        self.MAIN_CURRENCY_DROPDOWN = driver.find_element(
            *MainPageCurrencyLocators.MAIN_CURRENCY_DROPDOWN_LOCATOR
        )

    def getMainCurrencyVisibility(self):
        return self.MAIN_CURRENCY_VISIBILITY

    def getMainCurrencyDropdown(self):
        return self.MAIN_CURRENCY_DROPDOWN
