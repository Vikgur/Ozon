# Сомневающийся покупатель.

import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import *
from Page_Elements.MainPage import MainPage
from Page_Elements.DetailPage import DetailPageProduct
from Page_Elements.CatalogPageCleaner import CatalogPageCleaner
from Page_Elements.CartPageProducts import CartPageOneProduct, CartPageDeleteConfirm
from Locators.locators import CatalogPageCleanerLocators
from Tests.test_1_Smoke import authorisation_page_check

# Создать переменную начала выполнения кода.
start_time = time.time()

# Создать объект класса ActionChains.
action = ActionChains(driver)

# Создать объект класса Scrolls.
scrolls = Scrolls(driver, action)

# Передать управление страницей драйверу.
driver.get("https://www.ozon.ru/")
time.sleep(5)

# Создать объект главной страницы класса MainDetailCart.
main_page = MainPage(driver)

# Ввести запрос в строку поиска и выполнить поиск.
wait.until(EC.element_to_be_clickable(main_page.MAIN_SEARCH)).click()
time.sleep(1)
main_page.MAIN_SEARCH.send_keys("пылесос")
time.sleep(2)
main_page.MAIN_SEARCH.send_keys(Keys.ENTER)
time.sleep(2)


# Создать функцию добавления товара из каталога в корзину.
def add_product_to_cart():
    # Создать объект страницы каталога "пылесос" класса MainDetailCart.
    catalog_page = CatalogPageCleaner(driver)

    # В фильтре выбрать "робот-пылесос".
    wait.until(EC.element_to_be_clickable(catalog_page.FILTER_ROBOT_CLEANER)).click()
    time.sleep(2)

    # Создать объект страницы каталога "пылесос" класса MainDetailCart.
    catalog_page = CatalogPageCleaner(driver)

    # Кликнуть на первый робот-пылесос из результатов поиска.
    action.click(on_element=catalog_page.ROBOT_CLEANER_FIRST_RESULT).perform()
    time.sleep(3)

    # Переключить драйвер на вторую вкладку с товаром.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # После переключения драйвера на вторую вкладку.
    # создать объект страницы деталировки товара класса DetailPage.
    detail_page = DetailPageProduct(driver)

    # Кликнуть на кнопку "Перейти к описанию".
    action.click(on_element=detail_page.GO_TO_DESCRIPTION).perform()
    time.sleep(2)

    # Кликнуть на кнопку "Добавить в корзину".
    action.click(on_element=detail_page.PRODUCT_ADD_TO_CART).perform()
    time.sleep(2)

    # Кликнуть на кнопку иконки корзины в шапке справа.
    action.click(on_element=detail_page.ADD_TO_CART_ICON).perform()
    time.sleep(2)


# Добавить товар в корзину.
add_product_to_cart()

# Создать объект страницы корзины класса DetailPage.
cart_page = CartPageOneProduct(driver)

# Кликнуть на кнопку "Удалить выбранные".
wait.until(EC.element_to_be_clickable(cart_page.DELETE_ALL_SELECTED)).click()
time.sleep(3)

# Создать объект страницы корзины подтверждения
# удаления продуктов класса DetailPage.
cart_page_delete_confirm = CartPageDeleteConfirm(driver)

# Кликнуть на кнопку "Удалить".
wait.until(EC.element_to_be_clickable(cart_page_delete_confirm.DELETE_CONFIRM)).click()
time.sleep(2)

# Создать переменную для проверки наличия текста "Корзина пуста".
VISIBILITY_CART_EMPTY_TEXT = driver.find_elements(
    "xpath", "//span[normalize-space(.)='Корзина пуста']"
)

# Проверить через assert наличиt текста "Корзина пуста".
assert len(VISIBILITY_CART_EMPTY_TEXT) > 0, "Страница пустой корзины не открылась :-("

# Проверить через print наличиt текста "Корзина пуста".
if len(VISIBILITY_CART_EMPTY_TEXT) > 0:
    print(
        "Корзина пустая, первый товар удален!\nПользователь успешно начал второй поиск!"
    )
else:
    print("Страница пустой корзины не открылась :-(")
time.sleep(2)

# Вернуться на 1 историю браузера назад.
driver.back()
time.sleep(2)

# Закрыть текущую вкладку.
driver.close()
time.sleep(3)

# Переключить драйвер на оставшуюся вкладку.
tabs = driver.window_handles
driver.switch_to.window(tabs[0])

# Создать объект страницы каталога "пылесос" класса MainDetailCart.
catalog_page = CatalogPageCleaner(driver)

# Скроллить до фильтра "Сроки доставки".
scrolls.scroll_to_center(catalog_page.FILTER_DELIVERY_TIME)
time.sleep(2)

# Кликнуть radiobutton "До 3 дней".
wait.until(
    EC.element_to_be_clickable(catalog_page.FILTER_DELIVERY_TIME_3_DAYS_CLICK)
).click()
time.sleep(2)

# Создать переменную для проверки подтверждения
# выбора radiobutton "До 3 дней".
CONFIRM_3_DAYS_SELECTED = driver.find_element(
    *CatalogPageCleanerLocators.FILTER_DELIVERY_TIME_3_DAYS_CHECK_LOCATOR
)

# Проверить через assert, что radiobutton "До 3 дней" выбран.
assert CONFIRM_3_DAYS_SELECTED.is_selected(), 'Radiobutton "До 3 дней" не выбран :-('

# Проверить через print, что radiobutton "До 3 дней" выбран.
if CONFIRM_3_DAYS_SELECTED.is_selected():
    print("Фильтр 'До 3 дней' успешно выбран!")
else:
    print("Фильтр 'До 3 дней' не выбран :-(")

# Скроллить до фильтра "Бренд".
scrolls.scroll_to_center(catalog_page.FILTER_BRAND)
time.sleep(2)

# Кликнуть на бренд "Xiaomi".
wait.until(EC.element_to_be_clickable(catalog_page.FILTER_BRAND_XIAOMI)).click()
time.sleep(2)

# Скроллить до фильтра "Цена".
scrolls.scroll_to_center(catalog_page.FILTER_PRICE)
time.sleep(2)

# Кликнуть на поле ввода цены "от".
action.double_click(catalog_page.FILTER_PRICE_INPUT_FROM).perform()
time.sleep(2)

# Создать переменную для работы с полем ввода цены "от".
PRICE_INPUT_FROM = driver.find_element(
    *CatalogPageCleanerLocators.FILTER_PRICE_INPUT_FROM_LOCATOR
)

# Очистить поле ввода цены "от".
PRICE_INPUT_FROM.send_keys(Keys.BACKSPACE)
time.sleep(2)

# Ввести "30000" в поле ввода цены "от".
PRICE_INPUT_FROM.send_keys("30000")
time.sleep(2)

# Кликнуть на поле ввода цены "до".
action.click(catalog_page.FILTER_PRICE_INPUT_TO).perform()
time.sleep(2)

# Повторно кликнуть на поле ввода цены "до".
action.double_click(catalog_page.FILTER_PRICE_INPUT_TO).perform()
time.sleep(2)

# Создать переменную для работы с полем ввода цены "до".
PRICE_INPUT_TO = driver.find_element(
    *CatalogPageCleanerLocators.FILTER_PRICE_INPUT_TO_LOCATOR
)

# Очистить поле ввода цены "до".
PRICE_INPUT_TO.send_keys(Keys.BACKSPACE)
time.sleep(2)

# Ввести "60000" в поле ввода цены "до".
PRICE_INPUT_TO.send_keys("60000")
time.sleep(2)
PRICE_INPUT_TO.send_keys(Keys.ENTER)
time.sleep(2)
action.click(on_element=catalog_page.FILTER_PRICE).perform()
time.sleep(2)

# Скроллить до фильтра "Оригинальный товар".
scrolls.scroll_to_center(catalog_page.FILTER_ORIGINAL)
time.sleep(2)

# Кликнуть на "Оригинальный товар".
action.click(on_element=catalog_page.FILTER_ORIGINAL).perform()
time.sleep(2)

# Скроллить до фильтра "Оригинальный товар".
scrolls.scroll_to_center(catalog_page.FILTER_ORIGINAL)
time.sleep(2)

# Создать переменную для проверки подтверждения
# выбора "Оригинальный товар".
CONFIRM_ORIGINAL_SELECTED = driver.find_element(
    "xpath", "//input[@class='c7014-a0 c7014-a5']"
)

# Проверить через assert, что "Оригинальный товар" выбран.
assert CONFIRM_ORIGINAL_SELECTED.is_selected(), '"Оригинальный товар" не выбран :-('

# Проверить через print, что "Оригинальный товар" выбран.
if CONFIRM_ORIGINAL_SELECTED.is_selected():
    print("Фильтр 'Оригинальный товар' успешно выбран!")
else:
    print("Фильтр 'До 3 дней' не выбран :-(")

# Скроллить до фильтра "Вид пылесборника".
scrolls.scroll_to_center(catalog_page.FILTER_DUST_COLLECTOR)
time.sleep(2)

# Кликнуть на чек-бокс "Контейнер" в фильтре "Вид пылесборника".
action.click(on_element=catalog_page.FILTER_DUST_COLLECTOR).perform()
time.sleep(1)
action.click(on_element=catalog_page.FILTER_DUST_CHECKBOX_CONTAINER).perform()
time.sleep(2)

# Создать переменную для проверки подтверждения выбора чек-бокса "Контейнер".
CONFIRM_CONTAINER_SELECTED = ("xpath", "//input[@class='b4014-a0 b4014-a9']")

# Проверить через assert, что чек-бокс "Контейнер" выбран.
assert (
    driver.find_element(*CONFIRM_CONTAINER_SELECTED).get_attribute("checked") == "true"
), 'Чек-бокс "Контейнер" не выбран :-('

# Проверить через print, что чек-бокс "Контейнер" выбран.
if driver.find_element(*CONFIRM_CONTAINER_SELECTED).get_attribute("checked") == "true":
    print('Чек-бокс "Контейнер" успешно выбран!')
else:
    print('Чек-бокс "Контейнер" не выбран :-(')


# Кликнуть на чек-бокс "Аквафильтр" в фильтре "Вид пылесборника".
action.click(on_element=catalog_page.FILTER_DUST_COLLECTOR).perform()
time.sleep(1)
action.click(on_element=catalog_page.FILTER_DUST_CHECKBOX_AQUA).perform()
time.sleep(2)

# Создать переменную для проверки подтверждения выбора чек-бокса "Аквафильтр".
CONFIRM_AQUA_SELECTED = ("xpath", "//input[@class='b4014-a0 b4014-a9']")

# Проверить через assert, что чек-бокс "Аквафильтр" выбран.
assert (
    driver.find_element(*CONFIRM_AQUA_SELECTED).get_attribute("checked") == "true"
), 'Чек-бокс "Аквафильтр" не выбран :-('

# Проверить через print, что чек-бокс "Аквафильтр" выбран.
if driver.find_element(*CONFIRM_AQUA_SELECTED).get_attribute("checked") == "true":
    print('Чек-бокс "Аквафильтр" успешно выбран!')
else:
    print('Чек-бокс "Аквафильтр" не выбран :-(')

# Скроллить вверх к шапке.
scrolls.scroll_to_top()
time.sleep(2)

# Кликнуть на фильтр сортировки.
action.click(on_element=catalog_page.SORTED).perform()
time.sleep(2)

# Выбрать сортировку "С высоким рейтингом".
HIGH_RATING = driver.find_element(
    *("xpath", "//span[normalize-space(.)='С высоким рейтингом']")
)
action.click(on_element=HIGH_RATING).perform()
time.sleep(3)

# Создать переменную для проверки выбора сортировки "С высоким рейтингом".
CONFIRM_HIGH_RATING = driver.find_elements(
    *("xpath", "//input[@title='С высоким рейтингом']")
)

# Проверить через assert, что выбрана сортировка "С высоким рейтингом".
assert len(CONFIRM_HIGH_RATING) > 0, 'Сортировка "С высоким рейтингом" не выбрана :-('

# Проверить через print, что выбрана сортировка "С высоким рейтингом".
if len(CONFIRM_HIGH_RATING) > 0:
    print('Сортировка "С высоким рейтингом" успешно выбрана!')
else:
    print('Сортировка "С высоким рейтингом" не выбрана :-(')

time.sleep(2)

# Создать переменные для проверки применения всех фильтров.
CONFIRM_DELIVERY = driver.find_elements(
    *("xpath", "//span[normalize-space(.)='Сроки доставки: До 3 дней']")
)
CONFIRM_BRAND = driver.find_elements(
    *("xpath", "//span[normalize-space(.)='Бренд: Xiaomi']")
)
CONFIRM_PRICE = driver.find_elements(
    *("xpath", "//span[normalize-space(.)='Цена: от 30 000 до 60 000']")
)
CONFIRM_ORIGINAL = driver.find_elements(
    *("xpath", "//span[normalize-space(.)='Оригинальный товар']")
)
CONFIRM_DUST_CONTAINER = driver.find_elements(
    *("xpath", "//span[normalize-space(.)='Вид пылесборника: Контейнер']")
)
CONFIRM_DUST_AQUA = driver.find_elements(
    *("xpath", "//span[normalize-space(.)='Вид пылесборника: Аквафильтр']")
)

# Проверить через assert, что все выбраннные фильтры применились.
assert (
    len(CONFIRM_DELIVERY) > 0
    and len(CONFIRM_BRAND) > 0
    and len(CONFIRM_PRICE) > 0
    and len(CONFIRM_ORIGINAL) > 0
    and len(CONFIRM_DUST_CONTAINER) > 0
    and len(CONFIRM_DUST_AQUA) > 0
), "Какие-то фильтры не применились :-("

# Проверить через print, что все выбраннные фильтры применились.
if (
    len(CONFIRM_DELIVERY) > 0
    and len(CONFIRM_BRAND) > 0
    and len(CONFIRM_PRICE) > 0
    and len(CONFIRM_ORIGINAL) > 0
    and len(CONFIRM_DUST_CONTAINER) > 0
    and len(CONFIRM_DUST_AQUA) > 0
):
    print("Все фильтры успешно применились!")
else:
    print("Какие-то фильтры не применились :-(")

time.sleep(1)

# Добавить товар в корзину.
add_product_to_cart()

# Создать объект страницы корзины класса DetailPage.
cart_page = CartPageOneProduct(driver)

# Кликнуть на кнопку "Перейти к оформлению".
action.click(on_element=cart_page.CLICK_TO_BUY).perform()
time.sleep(2)

# Проверить переход на страницу авторизации.
authorisation_page_check()

driver.quit()

print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
