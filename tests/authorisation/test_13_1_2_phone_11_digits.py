# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation.test_13_1_1_phone_valid_phone import valid_steps

# Ввести цифру 99999999999 в поле ввода номера телефона.
authorisation_window.PHONE_INPUT_FIELD.send_keys(99999999999)
time.sleep(2)

# Проверить корректную работу с валидным значением.
valid_steps()

driver.quit()
