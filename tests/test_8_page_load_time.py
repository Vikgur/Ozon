import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
import requests

# Создать переменную временной разницы между
# отправкой запроса на url и получением ответа.
time_delta = requests.get("https://www.ozon.ru/")

# Вывести через print результат time_delta
# в секундах с округлением тысячных.
print(f"Результат: {round(time_delta.elapsed.total_seconds(), 3)} секунд")

driver.quit()

print("ТЕСТ ПРОЙДЕН УСПЕШНО!")
