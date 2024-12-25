import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
import os


@allure.description(
    "Ожидаемый результат: в отдельную директорию сохранился файл с html-кодом текущей страницы."
)
@allure.tag("Главная страница")
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-7", name="Получение атрибутов страницы")
def test_get_attributes():
    # Передать управление страницей драйверу.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # Создать переменную для передачи текущего url.
    url = driver.current_url

    # Проверить через print, что главная страница открыта корректно.
    print("URL текущей страницы:", url)

    # Создать объект для получения заголовка Title текущей страницы.
    current_title = driver.title

    # Проверить через assert заголовок Title текущей страницы.
    assert (
        current_title == "OZON маркетплейс – миллионы товаров по выгодным ценам"
    ), "Ошибка в title, неверный заголовок :-("

    # Проверить через print заголовок Title текущей страницы.
    print("Текущий заголовок:", current_title)

    # Создать объект для получения html-кода текущей страницы.
    current_page_source = driver.page_source

    # Скачать в папку page_source html-код текущей страницы.
    with open(
        os.getcwd() + "/Tests/page_source/page_source.html", "w", encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

    driver.quit()
