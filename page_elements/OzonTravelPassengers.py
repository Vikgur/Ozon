# Главная страница Ozon Travel выбор "Пассажиры и класс".

from locators.locators import OzonTravelPassengersLocators


class OzonTravelPassengers(object):

    def __init__(self, driver):

        # Выбор "Пассажиры и класс".
        self.INPUT_PASSENGERS_NEWBORN_ADD = driver.find_element(
            *OzonTravelPassengersLocators.INPUT_PASSENGERS_NEWBORN_ADD_LOCATOR
        )
        # Кнопка "Бизнес" в "Пассажиры и класс".
        self.INPUT_PASSENGERS_CLASS_BUSINESS = driver.find_element(
            *OzonTravelPassengersLocators.INPUT_PASSENGERS_CLASS_BUSINESS_LOCATOR
        )
