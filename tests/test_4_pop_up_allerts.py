import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.Allerts import Allerts
from locators.locators import AllertsLocators

@allure.description(
    "Ожидаемый результат: уведомление о Куках появилось и после клика на кнопку «ОК» скрылось."
)
@allure.tag("Главная страница")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase(
    "Ozon-4", name="Проверка всплывающих уведомлений"
)
def test_pop_up_allerts():
    # Передать управление страницей драйверу.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # После запуска драйвера и открытия главной страницы
    # создать объект управления уведомлениями класса AllertsPage.
    allerts = Allerts(driver)

    # Создать функцию проверки видимости элемента на странице
    # и вывода результата на экран.
    def visibility_check(button):
        try:
            if len(button) > 0:
                print("Уведомление появилось! ТЕСТ проходит успешно.")
            else:
                print("Уведомления нет :-(")
        except:
            pass

    # Создать функцию проверки невидимости элемента на странице
    # и вывода результата на экран.
    def invisibility_check(button):
        try:
            if len(button) > 0:
                print("Уведомление не отключено :-(")
            else:
                print("Уведомление отключилось! ТЕСТ ПРОЙДЕН УСПЕШНО!")
        except:
            pass

    # Создать переменные для проверки
    # наличия локаторов уведомлений после появления.
    # VISIBILITY_GEO_BEFORE_CLICK = driver.find_elements(
    #     *AllertsLocators.VISIBILITY_ALLERT_GEOLOCATION_LOCATOR
    # )
    VISIBILITY_COOKIES_BEFORE_CLICK = driver.find_elements(
        *AllertsLocators.VISIBILITY_ALLERT_COOKIE_LOCATOR
    )

    # # Проверить через assert появление уведомления о смене геолокации.
    # assert len(VISIBILITY_GEO_BEFORE_CLICK) > 0, "Выпадающий список/меню не появился :-("

    # # Проверить через print появление уведомления о смене геолокации.
    # visibility_check(VISIBILITY_GEO_BEFORE_CLICK)

    # Проверить через assert появление уведомления о куках.
    assert (
        len(VISIBILITY_COOKIES_BEFORE_CLICK) > 0
    ), "Выпадающий список/меню не появился :-("

    # Проверить через print появление уведомления о куках.
    visibility_check(VISIBILITY_COOKIES_BEFORE_CLICK)

    # # Отключить уведомления о геолокации.
    # wait.until(EC.element_to_be_clickable(allerts.SKIP_ALLERT_GEOLOCATION)).click()
    # time.sleep(2)

    # Отключить уведомления о куках.
    wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
    time.sleep(2)

    # Создать переменные для проверки
    # наличия локаторов уведомлений после отключения.
    # VISIBILITY_GEO_AFTER_CLICK = driver.find_elements(
    #     *AllertsLocators.VISIBILITY_ALLERT_GEOLOCATION_LOCATOR
    # )
    VISIBILITY_COOKIES_AFTER_CLICK = driver.find_elements(
        *AllertsLocators.VISIBILITY_ALLERT_COOKIE_LOCATOR
    )

    # # Проверить через assert отключение уведомления о смене геолокации.
    # assert len(VISIBILITY_GEO_AFTER_CLICK) == 0, "Выпадающий список/меню не появился :-("

    # # Проверить через print отключение уведомления о смене геолокации.
    # invisibility_check(VISIBILITY_GEO_AFTER_CLICK)

    # Проверить через assert отключение уведомления о куках.
    assert (
        len(VISIBILITY_COOKIES_AFTER_CLICK) == 0
    ), "Выпадающий список/меню не появился :-("

    # Проверить через print отключение уведомления о куках.
    invisibility_check(VISIBILITY_COOKIES_AFTER_CLICK)

    driver.quit()
