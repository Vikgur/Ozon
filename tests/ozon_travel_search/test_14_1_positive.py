import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.OzonTravel import OzonTravel
from tests.ozon_travel_search.test_filling_ticket_all_fields import filling_ticket_all_fields


def test_positive():
    # Заполнить все поля.
    filling_ticket_all_fields()

    # Создать объект класса ActionChains.
    action = ActionChains(driver)

    # После запуска драйвера создать объект
    # страницы класса OzonTravel.
    ozon_page = OzonTravel(driver)

    # Кликнуть на кнопку "Найти билеты".
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(1)
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(5)

    # Переключить драйвер на вторую вкладку с товаром.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Создать переменные локатора и элемента кнопки "Показать график цен"
    # на открывшейся странице результатов поиска.
    SHOW_PRICE_CHART_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Показать график цен']",
    )
    SHOW_PRICE_CHART = driver.find_element(*SHOW_PRICE_CHART_LOCATOR)

    # Проверить через assert открытие страницы результатов поиска.
    assert (
        SHOW_PRICE_CHART.text == "Показать график цен"
    ), "Страница с результатами поиска не открылась :-("

    # Проверить через print открытие страницы результатов поиска.
    if SHOW_PRICE_CHART.text == "Показать график цен":
        print("Страница с результатами поиска открылась!")
    else:
        print("Страница с результатами поиска не открылась :-(")

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

    driver.quit()
