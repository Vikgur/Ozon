# Импортировать опции драйвера и открыть окно авторизации.
from auth_window_imports_options import *

# Кликнуть на выпадающий список кодов.
wait.until(EC.element_to_be_clickable(authorisation_window.CODE_LIST)).click()
time.sleep(2)

# Создать переменную локатора кода страны "Соединенные штаты.
CODE_USA_LOCATOR = ("xpath", "//span[normalize-space(.)='Соединенные Штаты +1']")

# Создать переменную элемента кода страны "Соединенные штаты.
CODE_USA = driver.find_element(*CODE_USA_LOCATOR)

# Кликнуть на код страны "Соединенные штаты".
wait.until(EC.element_to_be_clickable(CODE_USA)).click()
time.sleep(2)

# Создать переменную локатора выбранного кода страны "Соединенные штаты".
CODE_USA_CHECK_LOCATOR = ("xpath", "//span[normalize-space(.)='+1']")

# Создать переменную наличия элемента
# выбранного кода страны "Соединенные штаты".
CODE_USA_CHECK = driver.find_elements(*CODE_USA_CHECK_LOCATOR)

# Проверить через assert, что выбран код страны "Соединенные штаты".
assert len(CODE_USA_CHECK) > 0, 'Код страны "Соединенные штаты" не выбран :-('

# Проверить через print, что выбран код страны "Соединенные штаты".
if len(CODE_USA_CHECK) > 0:
    print('Код страны "Соединенные штаты" выбран!')
else:
    print('Код страны "Соединенные штаты" не выбран :-(')

print("ТЕСТ ПРОЙДЕН УCПЕШНО!")

driver.quit()

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
