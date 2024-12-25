import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPage import MainPage
from page_elements.DetailPage import DetailPageBuyOneClick
from page_elements.AuthorisationPage import AuthorisationPage


# Создать функцию проверки открытия страницы авторизации.
def authorisation_page_check():

    # Создать локатор айфрейма.
    FIELD_IFRAME_LOCATOR = ("xpath", "//iframe[@id='authFrame']")

    # Переключить драйвер на айфрейм.
    driver.switch_to.frame("authFrame")

    # После перехода на страницу авторизации
    # создать объект страницы авторизации класса AuthorisationPage.
    authorisation_page = AuthorisationPage(driver)

    # Проверить через assert переход на страницу авторизации.
    assert (
        authorisation_page.VISIBILITY_TEXT_PHONE.text == "Введите номер телефона"
    ), "Переход на страницу Авторизация не осуществлен :-("

    # Проверить через print переход на страницу авторизации.
    if authorisation_page.VISIBILITY_TEXT_PHONE.text == "Введите номер телефона":
        print("Страница авторизации успешно открылась!")
    else:
        print("Страница авторизации не открыта :-(")


# Выполнить Smoke.
if __name__ == "__main__":

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

    driver.quit()

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")
