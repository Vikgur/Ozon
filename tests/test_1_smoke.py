import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPage import MainPage
from page_elements.DetailPage import DetailPageBuyOneClick
from authorisation_page_check import authorisation_page_check


@allure.description(
    "Ожидаемый результат: товар успешно добавится в корзину, но при попытке перейти к оформлению покупки пользователь попадет на страницу авторизации."
)
@allure.tag("Главная страница", "Страница деталировки", "Страница авторизации")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.issue("Ozon-bag-tracker-666", name="Не открывается страница авторизации")
@allure.testcase(
    "Ozon-1", name="Smoke тест — проверка работоспособности основного функционала"
)
def test_smoke():
    # Создать объект класса ActionChains.
    action = ActionChains(driver)

    # Создать объект класса Scrolls.
    scrolls = Scrolls(driver, action)

    # Передать управление страницей драйверу.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # После запуска драйвера и открытия главной страницы
    # создать объект главной страницы класса MainPage.
    main_page = MainPage(driver)

    # Скроллить до ближайшего товара с наименованием для клика.
    scrolls.scroll_to_center(main_page.MAIN_PRODUCT_1)
    time.sleep(2)

    # Кликнуть на первый товар раздела "Товары нарасхват"
    # Происходит переход на вторую вкладку с первым товаром.
    wait.until(EC.element_to_be_clickable(main_page.MAIN_PRODUCT_1)).click()
    time.sleep(2)

    # Переключить драйвер на вторую вкладку с товаром.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # После переключения драйвера на вторую вкладку
    # создать объект страницы деталировки товара класса DetailPage.
    detail_page = DetailPageBuyOneClick(driver)

    # На второй вкладке кликнуть на кнопку "Купить в один клик".
    # Происходит переход на страницу авторизации в этом же окне.
    action.click(on_element=detail_page.BUY_1_CLICK).perform()
    time.sleep(3)

    # Проверить переход на страницу авторизации.
    authorisation_page_check()

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

    driver.quit()
