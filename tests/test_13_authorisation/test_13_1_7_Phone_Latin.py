# Импортировать опции драйвера и открыть окно авторизации.
from auth_window_imports_options import *
from Tests.test_13_Authorisation.test_13_1_5_Phone_Empty_Field import valid_empty_steps

# Ввести "w" в поле ввода номера телефона.
authorisation_window.PHONE_INPUT_FIELD.send_keys("w")
time.sleep(2)

# Проверрить корректную работу с пустым полем ввода номера телефона.
valid_empty_steps()

driver.quit()

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
