import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPage import MainPage
from page_elements.DetailPage import DetailPageInDemand

# Тест-сессия:
# с главной страницы добавить товары
# в корзину в количестве больше 1 единицы каждый.


class MainDetailCart(object):

    # Добавить 2 товара в корзину
    def two_products(self):
        # Инициализировать объект класса ActionChains.
        action = ActionChains(driver)

        # Инициализировать объект класса Scrolls.
        scrolls = Scrolls(driver, action)

        # Передать управление страницей драйверу.
        driver.get("https://www.ozon.ru/")
        time.sleep(3)

        # После запуска драйвера и открытия главной страницы
        # инициализировать объект главной страницы класса MainPage.
        main_page = MainPage(driver)

        # Скроллить до ближайшего товара с наименованием для клика.
        scrolls.scroll_to_center(main_page.MAIN_PRODUCT_1)
        time.sleep(1)

        # Кликнуть на первый товар раздела "Товары нарасхват".
        # Происходит переход на вторую вкладку с первым товаром.
        wait.until(EC.element_to_be_clickable(main_page.MAIN_PRODUCT_1)).click()
        time.sleep(2)

        # Кликнуть на второй товар раздела "Товары нарасхват".
        # Происходит переход на третью вкладку со вторым товаром,
        wait.until(EC.element_to_be_clickable(main_page.MAIN_PRODUCT_2)).click()
        time.sleep(1)

        # Переключить драйвер на вторую вкладку с первым товаром.
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])

        # После переключения драйвера на вторую вкладку
        # инициализировать объект страницы деталировки товара DetailPage.
        detail_page = DetailPageInDemand(driver)

        # На второй вкладке добавить несколько единиц этого товара в корзину.
        wait.until(EC.element_to_be_clickable(detail_page.PRODUCT_ADD)).click()
        time.sleep(1)

        # Переключить драйвер на третью вкладку со вторым товаром и
        # инициализировать объект страницы деталировки товара DetailPage.
        driver.switch_to.window(tabs[2])
        detail_page = DetailPageInDemand(driver)

        # На третьей вкладке добавить несколько единиц этого товара в корзину.
        wait.until(EC.element_to_be_clickable(detail_page.PRODUCT_ADD)).click()
        time.sleep(1)

        # На третьей вкладке кликнуть на кнопку корзины в шапке справа.
        wait.until(EC.element_to_be_clickable(detail_page.ADD_TO_CART_ICON)).click()
        time.sleep(2)
