import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
import requests

@allure.description(
    "Ожидаемый результат: получен промежуток времени в виде разницы, прошедший между отправкой запроса и получением ответа."
)
@allure.tag("Главная страница")
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase(
    "Ozon-8", name="Тестирование производительности"
)
def test_page_load_time():
    # Создать переменную временной разницы между
    # отправкой запроса на url и получением ответа.
    time_delta = requests.get("https://www.ozon.ru/")

    # Вывести через print результат time_delta
    # в секундах с округлением тысячных.
    print(f"Результат: {round(time_delta.elapsed.total_seconds(), 3)} секунд")

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

    driver.quit()
