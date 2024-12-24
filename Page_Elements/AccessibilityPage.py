# Страница для слабовидящих.

from locators.locators import AccessibilityPageLocators


class MainPageFaceIcon(object):

    def __init__(self, driver):
        # Иконка авторизации/личный кабинет в виде "лица".
        self.VISIBILITY_FONT_CHANGE_OPTIONS = driver.find_element(
            *AccessibilityPageLocators.VISIBILITY_FONT_CHANGE_OPTIONS_LOCATOR
        )

    def getVisibilityFontChangeOptions(self):
        return self.VISIBILITY_FONT_CHANGE_OPTIONS
