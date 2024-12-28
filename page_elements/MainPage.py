# Главная страница.

from locators.locators import MainPageLocators


class MainPage(object):

    def __init__(self, driver):
        self.driver = driver
        # Первая категория товаров с наименованиями в виде ссылок.
        self.MAIN_FIRST_CATEGORY = driver.find_element(
            *MainPageLocators.MAIN_FIRST_CATEGORY_LOCATOR
        )
        # Первый товар.
        self.MAIN_PRODUCT_1 = driver.find_element(
            *MainPageLocators.MAIN_PRODUCT_1_LOCATOR
        )
        # Второй товар.
        self.MAIN_PRODUCT_2 = driver.find_element(
            *MainPageLocators.MAIN_PRODUCT_2_LOCATOR
        )
        # Кнопка "RUB" в шапке.
        self.MAIN_CURRENCY = driver.find_element(
            *MainPageLocators.MAIN_CURRENCY_LOCATOR
        )
        # Иконка "Мои Заказы" в виде коробочки.
        self.MAIN_ORDER_LIST = driver.find_element(
            *MainPageLocators.MAIN_ORDER_LIST_LOCATOR
        )
        # Поле ввода в поисковую строку.
        self.MAIN_SEARCH = driver.find_element(*MainPageLocators.MAIN_SEARCH_LOCATOR)

    def getMainFirstCategory(self):
        return self.MAIN_FIRST_CATEGORY

    def getMainProduct1(self):
        return self.MAIN_PRODUCT_1

    def getMainProduct2(self):
        return self.MAIN_PRODUCT_2

    def getMainCurrency(self):
        return self.MAIN_CURRENCY

    def getMainSearch(self):
        return self.MAIN_SEARCH
