import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
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