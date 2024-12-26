# Иконка авторизации "Лицо" главной страницы в шапке.

from locators.locators import MainPageAuthorisationIconLocators


class MainPageAuthorisationIcon(object):

    def __init__(self, driver):
        # Иконка "Лицо".
        self.MAIN_FACE_ICON = driver.find_element(
            *MainPageAuthorisationIconLocators.MAIN_FACE_ICON_LOCATOR
        )

    def getMainFaceIcon(self):
        return self.MAIN_FACE_ICON
