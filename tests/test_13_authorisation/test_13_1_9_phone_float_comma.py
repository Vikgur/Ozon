# Импортировать опции драйвера и открыть окно авторизации.
from auth_window_imports_options import *
from tests.test_13_authorisation.test_13_1_1_phone_valid_phone import valid_steps

# Ввести цифру 9,999999999 в поле ввода номера телефона.
authorisation_window.PHONE_INPUT_FIELD.send_keys("9,999999999")
time.sleep(2)

# Проверить корректную работу с валидным значением.
valid_steps()

driver.quit()

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
