import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.OzonTravel import OzonTravel
from tests.ozon_travel_search.test_filling_ticket_all_fields import (
    filling_ticket_all_fields,
)


@allure.description(
    "Ожидаемый результат: после ввода всех данных для покупки билета и очистки поля «Куда» появится ошибка «Заполните поле» и страница с результатами поиска не открылась."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-14.2", name="Негативный тест")
def test_negative():
    # Создать объект класса ActionChains.
    action = ActionChains(driver)

    # Заполнить все поля.
    filling_ticket_all_fields()

    # Cоздать объект страницы класса OzonTravel.
    ozon_page = OzonTravel(driver)

    # Очистить поле ввода "Куда".
    action.click(ozon_page.INPUT_TO).perform()
    time.sleep(1)
    action.click(ozon_page.INPUT_TO).perform()
    time.sleep(2)

    # Кликнуть на кнопку "Найти билеты".
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(1)
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(3)

    # Создать переменные локатора и элемента уведомления "Заполните поле".
    ERROR_NOTIFICATION_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Заполните поле']",
    )
    ERROR_NOTIFICATION = driver.find_element(*ERROR_NOTIFICATION_LOCATOR)

    # Проверить через assert появление ошибки "Заполните поле".
    assert (
        ERROR_NOTIFICATION.text == "Заполните поле"
    ), 'Ошибка "Заполните поле" не появилась :-('

    # Проверить через print появление ошибки "Заполните поле".
    if ERROR_NOTIFICATION.text == "Заполните поле":
        print('Ошибка "Заполните поле" появилась!')
    else:
        print('Ошибка "Заполните поле" не появилась :-(')

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

    driver.quit()
