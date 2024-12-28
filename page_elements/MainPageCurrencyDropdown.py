# Выпадающий список модального неблокирующего окна "Валюта".

from locators.locators import MainPageCurrencyDropdownLocators


class MainPageСurrencyDropdown(object):

    def __init__(self, driver):
        # Доллар США.
        self.MAIN_CURRENCY_DROPDOWN_USD = driver.find_element(
            *MainPageCurrencyDropdownLocators.MAIN_CURRENCY_DROPDOWN_USD_LOCATOR
        )

    def getMainCurrencyDropdownUsd(self):
        return self.MAIN_CURRENCY_DROPDOWN_USD
