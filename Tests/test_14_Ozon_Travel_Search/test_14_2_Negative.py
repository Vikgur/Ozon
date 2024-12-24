import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.OzonTravel import OzonTravel
from test_14_1_positive import positive_fill

# Создать переменную начала выполнения кода.
start_time = time.time()

# Создать объект класса ActionChains.
action = ActionChains(driver)

# Заполнить все поля.
positive_fill()

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
ERROR_NOTIFICATION_LOCATOR = ("xpath", "//span[normalize-space(.)='Заполните поле']")
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

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
