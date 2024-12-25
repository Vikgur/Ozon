import sys

sys.path.append(sys.path[0] + "/..")
import os
import pickle
from imports_options import *
from page_elements.CartPageProducts import CartPageTwoProducts
from locators.locators import CartPageTwoProductLocators
from main_detail_cart import MainDetailCart


@allure.description(
    "Ожидаемый результат: после добавления двух разных наименований товаров в корзину и очистки куков товары пропадут из корзины, а после восстановления удаленных куков эти же товары в том же количестве вернутся в корзину."
)
@allure.tag("Главная страница", "Страница деталировки", "Страница корзины")
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-6", name="Тестирование работы cookies")
def test_cookies():
    # Создать объект для добавления с главной страницы
    # 2 товаров в корзину класса MainDetailCart.
    main_detail_cart = MainDetailCart()

    # Добавить с главной страницы 2 товара в корзину
    main_detail_cart.two_products()

    # После переключения драйвера на третью вкладку
    # создать объект страницы корзины CartPage.
    cart_page = CartPageTwoProducts(driver)

    # Проверить через assert, что текущая страница - страница корзины.
    assert driver.title == "OZON.ru - Моя корзина", "Открыта не та страница :-("

    # Скачать все куки со страницы корзины в файл cookies.pkl в директорию test_cookies.
    pickle.dump(
        driver.get_cookies(),
        open(os.getcwd() + "/Tests/test_cookies/cookies.pkl", "wb"),
    )

    # Удалить все куки.
    driver.delete_all_cookies()

    # Обновить страницу.
    driver.refresh()

    # Повторно запустить удаление куков на случай,
    # если с первого раза куки не удалились.
    driver.delete_all_cookies()

    # Повторно обновить страницу.
    driver.refresh()

    # Создать переменные для проверки
    # наличия на странице цены на каждый товар.
    VISIBILITY_PRODUCT_PRICE_1 = driver.find_elements(
        *CartPageTwoProductLocators.CART_PRODUCT_1_PRICE_LOCATOR
    )
    VISIBILITY_PRODUCT_PRICE_2 = driver.find_elements(
        *CartPageTwoProductLocators.CART_PRODUCT_2_PRICE_LOCATOR
    )

    # Проверить через assert наличие видимости цены на каждый товар.
    assert len(VISIBILITY_PRODUCT_PRICE_1) == 0, "Товар 1 не удален :-("
    assert len(VISIBILITY_PRODUCT_PRICE_2) == 0, "Товар 2 не удален :-("

    # Проверить через print наличие видимости цены на каждый товар.
    if len(VISIBILITY_PRODUCT_PRICE_1) > 0 and len(VISIBILITY_PRODUCT_PRICE_2) > 0:
        print("Товары все еще в корзине :-(")
    else:
        print("Товаров в корзине нет: КУКИ УСПЕШНО УДАЛЕНЫ!")

    time.sleep(3)

    # Восстанавить сессию в корзине с двумя добавленными
    # ранее товарами, удаленными через очистку куков.
    cookies = pickle.load(open(os.getcwd() + "/Tests/test_cookies/cookies.pkl", "rb"))

    for cookie in cookies:
        driver.add_cookie(cookie)

    # Обновить страницу после восстановления куков.
    driver.refresh()
    time.sleep(3)

    # Создать переменные для проверки
    # наличия на странице цены на каждый товар.
    VISIBILITY_PRODUCT_PRICE_1_RESTORED = driver.find_elements(
        *CartPageTwoProductLocators.CART_PRODUCT_1_PRICE_LOCATOR
    )
    VISIBILITY_PRODUCT_PRICE_2_RESTORED = driver.find_elements(
        *CartPageTwoProductLocators.CART_PRODUCT_2_PRICE_LOCATOR
    )

    # Проверить через assert наличие видимости цены на каждый товар.
    assert len(VISIBILITY_PRODUCT_PRICE_1_RESTORED) > 0, "Товар 1 не восстановлен :-("
    assert len(VISIBILITY_PRODUCT_PRICE_2_RESTORED) > 0, "Товар 2 не восстановлен :-("

    # Проверить через print наличие видимости цены на каждый товар.
    if (
        len(VISIBILITY_PRODUCT_PRICE_1_RESTORED) > 0
        and len(VISIBILITY_PRODUCT_PRICE_2_RESTORED) > 0
    ):
        print("Товары в корзине, куки восстановлены, ТЕСТ ПРОЙДЕН УСПЕШНО!")
    else:
        print("Товаров в корзине нет :-(")

    driver.quit()
