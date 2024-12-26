import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
import requests


@allure.description(
    "Ожидаемый результат: получен промежуток времени в виде разницы, прошедший между отправкой запроса и получением ответа в режиме работы браузера со включенным расширением."
)
@allure.tag("Главная страница")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase(
    "Ozon-9", name="9. Тестирование производительности при любом запущенном расширении"
)
def test_extension_page_load_time():
    # Установить необходимое расширение.
    chrome_options.add_extension("Tests/Extensions/adblock.crx")

    # Создать новый объект драйвера, который откроет второе окно.
    driver = webdriver.Chrome(options=chrome_options)

    # Создать переменную главной страницы сайта.
    url = "https://www.ozon.ru/"

    # Открыть главную страницу сайта.
    driver.get(url)
    time.sleep(5)

    # Создать переменную временной разницы между
    # отправкой запроса на url и получением ответа.
    time_delta = requests.get(url)

    # Вывести через print результат time_delta
    # в секундах с округлением до тысячных.
    print(f"Результат: {round(time_delta.elapsed.total_seconds(), 3)} секунд")

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

    driver.quit()
