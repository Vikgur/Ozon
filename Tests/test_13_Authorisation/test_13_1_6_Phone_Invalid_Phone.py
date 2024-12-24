# Импортировать опции драйвера и открыть окно авторизации.
from auth_window_imports_options import *
from tests.test_13_authorisation.test_13_1_3_phone_9_digits import valid_error_steps

# Ввести цифру 1111111111 в поле ввода номера телефона.
authorisation_window.PHONE_INPUT_FIELD.send_keys(1111111111)
time.sleep(2)

# Проверить корректную работу с валидным ошибочным значением.
valid_error_steps()

driver.quit()

print("ТЕСТ ПРОЙДЕН УПЕШНО!")

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
