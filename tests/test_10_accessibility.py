import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPageBottom import MainPageBottom
from page_elements.Allerts import Allerts
from locators.locators import AccessibilityPageLocators

@allure.description(
    "Ожидаемый результат: после клика на на кнопку «Для слабовидящих» происходит переход на страницу для слабовидящих."
)
@allure.tag("Главная страница", "Страница для слабовидящих")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase(
    "Ozon-10", name="Тестирование доступности"
)
def test_accessebility():
    # Создать объект класса ActionChains.
    action = ActionChains(driver)

    # Создать объект класса Scrolls.
    scrolls = Scrolls(driver, action)

    # Передать управление страницей драйверу.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # Создать объект управления уведомлениями класса AllertsPage.
    allerts = Allerts(driver)

    # Отключить уведомления о куках.
    wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
    time.sleep(2)

    # Скроллить в самый низ страницы к подвалу.
    scrolls.scroll_to_bottom()
    time.sleep(2)

    # Скроллить в самый низ страницы к подвалу.
    # Двойной скролл необходим в случае, если страница не успела прогрузиться.
    scrolls.scroll_to_bottom()
    time.sleep(2)

    # Создать объект подвала главной страницы класса MainPageBottom.
    main_page_bottom = MainPageBottom(driver)

    # Кликнуть на кнопку "Для слабовидящих".
    wait.until(EC.element_to_be_clickable(main_page_bottom.MAIN_ACCESSIBILITY)).click()
    time.sleep(3)

    # Создать переменную для проверки наличия локатора
    # опции изменения шрифта на странице для слабовидящих.
    VISIBILITY_FONT_OPTIONS = driver.find_elements(
        *AccessibilityPageLocators.VISIBILITY_FONT_CHANGE_OPTIONS_LOCATOR
    )

    # Проверить через assert открытие страницы для слабовидящих.
    assert len(VISIBILITY_FONT_OPTIONS) > 0, "Страница для слабовидящих не открылась :-("

    # Проверить через print открытие страницы для слабовидящих.
    if len(VISIBILITY_FONT_OPTIONS) > 0:
        print("Страница для слабовидящих открылась! ТЕСТ ВЫПОЛНЕН УСПЕШНО!")
    else:
        print("Страница для слабовидящих не открылась :-(")

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

    driver.quit()
