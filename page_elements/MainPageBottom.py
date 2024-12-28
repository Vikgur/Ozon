# Подвал.

from locators.locators import MainPageBottomLocators


class MainPageBottom(object):

    def __init__(self, driver):
        # Текст "Валюта".
        self.MAIN_ACCESSIBILITY = driver.find_element(
            *MainPageBottomLocators.MAIN_ACCESSIBILITY_LOCATOR
        )

    def getMainAccessibility(self):
        return self.MAIN_ACCESSIBILITY
