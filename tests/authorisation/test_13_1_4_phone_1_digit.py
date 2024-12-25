# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation.test_13_1_3_phone_9_digits import valid_error_steps

# Ввести цифру 1 в поле ввода номера телефона.
authorisation_window.PHONE_INPUT_FIELD.send_keys(1)
time.sleep(2)

# Проверить корректную работу с валидным ошибочным значением.
valid_error_steps()

driver.quit()

print("ТЕСТ ПРОЙДЕН УПЕШНО!")
