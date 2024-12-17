# Импортировать опции драйвера и открыть окно авторизации.
from auth_window_imports_options import *
from Tests.test_13_Authorisation.test_13_1_1_Phone_Valid_Phone import valid_steps

# Ввести цифру 99999999999 в поле ввода номера телефона.
authorisation_window.PHONE_INPUT_FIELD.send_keys(99999999999)
time.sleep(2)

# Проверить корректную работу с валидным значением.
valid_steps()

driver.quit()

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
