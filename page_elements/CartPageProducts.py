# Страница корзины с товарами.

from locators.locators import (
    CartPageOneProductLocators,
    CartPageTwoProductLocators,
    CartPageDeleteConfirmLocators,
)


# Одно наименование товара.
class CartPageOneProduct(object):

    def __init__(self, driver):
        self.driver = driver
        # Кнопка "Перейти к оформлению".
        self.CLICK_TO_BUY = driver.find_element(
            *CartPageOneProductLocators.CLICK_TO_BUY_LOCATOR
        )
        # Поле ввода изменения количества у первого товара.
        self.CART_INPUT_PRODUCTS_1 = driver.find_element(
            *CartPageOneProductLocators.CART_INPUT_PRODUCTS_1_LOCATOR
        )
        # Общая цена с Ozon Картой за 1 ед первого товара.
        self.CART_PRODUCT_1_PRICE = driver.find_element(
            *CartPageOneProductLocators.CART_PRODUCT_1_PRICE_LOCATOR
        )
        # Итоговая цена за оба товара с Ozon Картой.
        self.CART_TOTAL_PRICE = driver.find_element(
            *CartPageOneProductLocators.CART_TOTAL_PRICE_LOCATOR
        )
        # Кнопка "поделиться".
        self.SHARE_BUTTON = driver.find_element(
            *CartPageOneProductLocators.SHARE_BUTTON_LOCATOR
        )
        # Кнопка "Удалить выбранные".
        self.DELETE_ALL_SELECTED = driver.find_element(
            *CartPageOneProductLocators.DELETE_ALL_SELECTED_LOCATOR
        )

    def getClickToBuy(self):
        return self.CLICK_TO_BUY

    def getCartInputProductsOne(self):
        return self.CART_INPUT_PRODUCTS_1

    def getShareButton(self):
        return self.SHARE_BUTTON

    def getDeleteAllSelected(self):
        return self.DELETE_ALL_SELECTED


# Два наименования товаров.
class CartPageTwoProducts(CartPageOneProduct):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        # Поле ввода изменения количества у второго товара.
        self.CART_INPUT_PRODUCTS_2 = driver.find_element(
            *CartPageTwoProductLocators.CART_INPUT_PRODUCTS_2_LOCATOR
        )
        # Общая цена с Ozon Картой за 1 ед второго товара.
        self.CART_PRODUCT_2_PRICE = driver.find_element(
            *CartPageTwoProductLocators.CART_PRODUCT_2_PRICE_LOCATOR
        )

    def getCartInputProductsTwo(self):
        return self.CART_INPUT_PRODUCTS_2

    def getCartProductTwoPrice(self):
        return self.CART_PRODUCT_2_PRICE


# Окно подтверждения удаления товаров.
class CartPageDeleteConfirm(object):

    def __init__(self, driver):
        self.driver = driver
        # Кнопка "Удалить".
        self.DELETE_CONFIRM = driver.find_element(
            *CartPageDeleteConfirmLocators.DELETE_CONFIRM_LOCATOR
        )
