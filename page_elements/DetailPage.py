# Страница деталировки товара.

from locators.locators import (
    DetailPageLocators,
    DetailPageBuyOneClickLocators,
    DetailPageInDemandLocators,
    DetailPageProductLocators,
)


class DetailPage(object):

    def __init__(self, driver):
        self.driver = driver
        # Кнопка перехода в корзину в шапке справа.
        self.ADD_TO_CART_ICON = driver.find_element(
            *DetailPageLocators.ADD_TO_CART_ICON_LOCATOR
        )

    def getAddToCartIcon(self):
        return self.ADD_TO_CART_ICON


# С множественным выбором единиц товара.
class DetailPageInDemand(DetailPage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        # Кнопка добавления нескольких товаров.
        self.PRODUCT_ADD = driver.find_element(
            *DetailPageInDemandLocators.PRODUCT_ADD_LOCATOR
        )

    def getProductAdd(self):
        return self.PRODUCT_ADD


# С выбором 1 единицы товара.
class DetailPageProduct(DetailPage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        # Кнопка добавления нескольких товаров.
        self.PRODUCT_ADD_TO_CART = driver.find_element(
            *DetailPageProductLocators.PRODUCT_ADD_TO_CART_LOCATOR
        )
        # Текст категории Описание при прокрутке вниз.
        self.GO_TO_DESCRIPTION = driver.find_element(
            *DetailPageProductLocators.GO_TO_DESCRIPTION_LOCATOR
        )

    def getProductAddToCart(self):
        return self.PRODUCT_ADD_TO_CART


# C кнопкой "Купить в 1 клик"
class DetailPageBuyOneClick(DetailPage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        # Кнопка "Купить в один клик".
        self.BUY_1_CLICK = driver.find_element(
            *DetailPageBuyOneClickLocators.BUY_1_CLICK_LOCATOR
        )

    def getBuy1Click(self):
        return self.BUY_1_CLICK
