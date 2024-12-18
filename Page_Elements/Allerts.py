# Всплывающие pop-up уведомления.

from Locators.locators import AllertsLocators


class Allerts(object):

    def __init__(self, driver):
        self.driver = driver
        # Кнопка "ОК" принятия всплывающего аллерта о куках.
        self.ACCEPT_ALLERT_COOKIE = driver.find_element(
            *AllertsLocators.ACCEPT_ALLERT_COOKIE_LOCATOR
        )
        # Кнопка "ОК" принятия всплывающего аллерта о куках.
        self.SKIP_ALLERT_GEOLOCATION = driver.find_element(
            *AllertsLocators.SKIP_ALLERT_GEOLOCATION_LOCATOR
        )
        # Кнопка "ОК" принятия всплывающего аллерта о куках.
        self.VISIBILITY_ALLERT_GEOLOCATION = driver.find_element(
            *AllertsLocators.VISIBILITY_ALLERT_GEOLOCATION_LOCATOR
        )
        # Кнопка "ОК" принятия всплывающего аллерта о куках.
        self.VISIBILITY_ALLERT_COOKIE = driver.find_element(
            *AllertsLocators.VISIBILITY_ALLERT_COOKIE_LOCATOR
        )

    def getAcceptAllertCookie(self):
        return self.ACCEPT_ALLERT_COOKIE

    def getSkipAllertGeolocation(self):
        return self.SKIP_ALLERT_GEOLOCATION
