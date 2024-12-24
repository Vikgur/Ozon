import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.MainPage import MainPage
from page_elements.Allerts import Allerts
from page_elements.MainPageCurrency import MainPageСurrency
from page_elements.MainPageCurrencyDropdown import MainPageСurrencyDropdown
from locators.locators import MainPageCurrencyLocators, MainPageCurrencyDropdownLocators

# Создать переменную начала выполнения кода.
start_time = time.time()

# Создать объект класса ActionChains.
action = ActionChains(driver)

# Передать управление страницей драйверу.
driver.get("https://www.ozon.ru/")
time.sleep(5)

# Создать объект управления уведомлениями класса AllertsPage.
allerts = Allerts(driver)

# Отключить уведомления о куках.
wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
time.sleep(5)

# Создать объект главной страницы класса MainPage.
main_page = MainPage(driver)

# Кликнуть на кнопку "RUB" в шапке слева.
wait.until(EC.element_to_be_clickable(main_page.MAIN_CURRENCY)).click()
time.sleep(3)

# Создать объект окна "Валюта".
currency_page = MainPageСurrency(driver)

# Создать переменную для проверки перехода на модальное окно "Валюта".
VISIBILITY_CURRENCY = driver.find_elements(
    *MainPageCurrencyLocators.MAIN_CURRENCY_VISIBILITY_LOCATOR
)

# Проверить через assert открытие окна "Валюта".
assert len(VISIBILITY_CURRENCY) > 0, 'Окно "Валюта" не открылось :-('

# Проверить через print открытие окна "Валюта".
if len(VISIBILITY_CURRENCY) > 0:
    print('Окно "Валюта" открылось! ТЕСТ ПРОХОДИТ УСПЕШНО!')
else:
    print('Окно "Валюта" не открылось :-(')

# Создать переменную для клика на выпадающий список.
DROPDOWN = driver.find_element(*MainPageCurrencyLocators.MAIN_CURRENCY_DROPDOWN_LOCATOR)

# Кликнуть на DROPDOWN.
wait.until(EC.element_to_be_clickable(DROPDOWN)).click()
time.sleep(2)

# Класс Select для продолжения не применим из-за отсутствия дескриптора <select>.

# Создать объект выпадающего списка окна "Валюта".
currency_page_dropdown = MainPageСurrencyDropdown(driver)

# Создать переменную для выбора валюты Доллар Сша.
DOLLAR_USA = driver.find_element(
    *MainPageCurrencyDropdownLocators.MAIN_CURRENCY_DROPDOWN_USD_LOCATOR
)

# Кликнуть на Доллар США.
wait.until(EC.element_to_be_clickable(DOLLAR_USA)).click()
time.sleep(5)

# Создать переменную для проверки переключения валюты на USD.
CONFIRM_USD = driver.find_element("xpath", "//button[@data-widget='selectedCurrency']")

# Проверить через assert, что переключение на USD произошло.
assert CONFIRM_USD.text == "USD", "Валюта не USD :-("

# Проверить через print, что переключение на USD произошло.
if CONFIRM_USD.text == "USD":
    print(f"Валюта - {CONFIRM_USD.text}: ТЕСТ ПРОЙДЕН УСПЕШНО!")
else:
    print("Валюта не USD :-(")

driver.quit()

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
