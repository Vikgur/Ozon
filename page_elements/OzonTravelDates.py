# Главная страница Ozon Travel выбор "Даты".

from locators.locators import OzonTravelDatesLocators


class OzonTravelDates(object):

    def __init__(self, driver):
        # День 1 месяца Март в "Даты".
        self.INPUT_DATE_DAY = driver.find_element(
            *OzonTravelDatesLocators.INPUT_DATE_DAY_LOCATOR
        )
