# Каталог, поисковой запрос "пылесос".

from locators.locators import CatalogPageCleanerLocators


class CatalogPageCleaner(object):

    def __init__(self, driver):
        # Первый Робот-пылесос в поиске фильтра "Робот-пылесос".
        self.ROBOT_CLEANER_FIRST_RESULT = driver.find_element(
            *CatalogPageCleanerLocators.ROBOT_CLEANER_FIRST_RESULT_LOCATOR
        )
        # Текст "Валюта".
        self.FILTER_ROBOT_CLEANER = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_ROBOT_CLEANER_LOCATOR
        )
        # Фильтр "Срок доставки".
        self.FILTER_DELIVERY_TIME = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_DELIVERY_TIME_LOCATOR
        )
        # Проверка выбора "До 3 дней".
        self.FILTER_DELIVERY_TIME_3_DAYS_CHECK = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_DELIVERY_TIME_3_DAYS_CHECK_LOCATOR
        )
        # Клик на выбор "До 3 дней"
        self.FILTER_DELIVERY_TIME_3_DAYS_CLICK = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_DELIVERY_TIME_3_DAYS_CLICK_LOCATOR
        )
        # Фильтр "Бренд".
        self.FILTER_BRAND = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_BRAND_LOCATOR
        )
        # Фильтр "Бренд" Xiaomi.
        self.FILTER_BRAND_XIAOMI = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_BRAND_XIAOMI_LOCATOR
        )
        # Фильтр "Цена".
        self.FILTER_PRICE = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_PRICE_LOCATOR
        )
        # Фильтр "Цена" поле ввода "от".
        self.FILTER_PRICE_INPUT_FROM = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_PRICE_INPUT_FROM_LOCATOR
        )
        # Фильтр "Цена" поле ввода "до".
        self.FILTER_PRICE_INPUT_TO = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_PRICE_INPUT_TO_LOCATOR
        )
        # Фильтр "Оригинальный товар".
        self.FILTER_ORIGINAL = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_ORIGINAL_LOCATOR
        )
        # Фильтр "Вид пылесборника".
        self.FILTER_DUST_COLLECTOR = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_DUST_COLLECTOR_LOCATOR
        )
        # Чек-бокс "Контейнер" фильтра "Вид пылесборника".
        self.FILTER_DUST_CHECKBOX_CONTAINER = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_DUST_CHECKBOX_CONTAINER_LOCATOR
        )
        # Чек-бокс "Аквафильтр" фильтра "Вид пылесборника".
        self.FILTER_DUST_CHECKBOX_AQUA = driver.find_element(
            *CatalogPageCleanerLocators.FILTER_DUST_CHECKBOX_AQUA_LOCATOR
        )
        # Сортировка.
        self.SORTED = driver.find_element(*CatalogPageCleanerLocators.SORTED_LOCATOR)

    def getFilterRobotCleaner(self):
        return self.FILTER_ROBOT_CLEANER

    def getRobotCleanerFirstResult(self):
        return self.ROBOT_CLEANER_FIRST_RESULT
