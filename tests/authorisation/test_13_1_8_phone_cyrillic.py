# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation.test_13_1_5_phone_empty_field import valid_empty_steps

# Ввести "ж" в поле ввода номера телефона.
authorisation_window.PHONE_INPUT_FIELD.send_keys("ж")
time.sleep(2)

# Проверрить корректную работу с пустым полем ввода номера телефона.
valid_empty_steps()

driver.quit()
