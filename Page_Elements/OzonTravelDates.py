# Главная страница Ozon Travel выбор "Даты".

from Locators.locators import OzonTravelDatesLocators


class OzonTravelDates(object):

    def __init__(self, driver):

        # Месяц Март в "Даты".
        self.INPUT_DATE_MONTH_MARCH = driver.find_element(
            *OzonTravelDatesLocators.INPUT_DATE_MONTH_MARCH_LOCATOR
        )
        # День 1 месяца Март в "Даты".
        self.INPUT_DATE_DAY_1 = driver.find_element(
            *OzonTravelDatesLocators.INPUT_DATE_DAY_1_LOCATOR
        )

