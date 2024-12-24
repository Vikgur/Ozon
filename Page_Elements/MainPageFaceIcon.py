# Главная страница выпадающего списка иконки "Лицо".

from locators.locators import MainPageFaceIconLocators


class MainPageFaceIcon(object):

    def __init__(self, driver):
        # Иконка авторизации/личный кабинет в виде "лица".
        self.MAIN_FACE_ICON = driver.find_element(
            *MainPageFaceIconLocators.MAIN_FACE_ICON_LOCATOR
        )
        # Кнопка авторизации в иконке в виде "лица".
        self.MAIN_FACE_ICON_SIGN_IN = driver.find_element(
            *MainPageFaceIconLocators.MAIN_FACE_ICON_SIGN_IN_LOCATOR
        )
        # Кнопка перехода в личный кабинет в иконке в виде "лица".
        self.MAIN_FACE_ICON_ACCOUNT = driver.find_element(
            *MainPageFaceIconLocators.MAIN_FACE_ICON_ACCOUNT_LOCATOR
        )

    def getMainFaceIcon(self):
        return self.MAIN_FACE_ICON

    def getMainFaceIconSignIn(self):
        return self.MAIN_FACE_ICON_SIGN_IN

    def getMainFaceIconAccount(self):
        return self.MAIN_FACE_ICON_ACCOUNT
