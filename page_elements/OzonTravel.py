# Главная страница Ozon Travel.

from locators.locators import OzonTravelLocators


class OzonTravel(object):

    def __init__(self, driver):
        # Кнопка "х" очистки поля "Откуда".
        self.INPUT_FROM_CLEAR = driver.find_element(
            *OzonTravelLocators.INPUT_FROM_CLEAR_LOCATOR
        )
        # Поле ввода "Откуда".
        self.INPUT_FROM = driver.find_element(*OzonTravelLocators.INPUT_FROM_LOCATOR)
        # Поле ввода "Куда".
        self.INPUT_TO = driver.find_element(*OzonTravelLocators.INPUT_TO_LOCATOR)
        # Поле ввода "Даты".
        self.INPUT_DATE = driver.find_element(*OzonTravelLocators.INPUT_DATE_LOCATOR)
        # # Выбор "Пассажиры и класс".
        self.INPUT_PASSENGERS_CLASS = driver.find_element(
            *OzonTravelLocators.INPUT_PASSENGERS_CLASS_LOCATOR
        )
        # Кнопка "Найти билеты".
        self.FIND_TICKETS_BUTTON = driver.find_element(
            *OzonTravelLocators.FIND_TICKETS_BUTTON_LOCATOR
        )
