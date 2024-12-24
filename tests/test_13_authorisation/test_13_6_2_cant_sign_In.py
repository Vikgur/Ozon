# Импортировать опции драйвера, открыть окно авторизации.
# открыть окно "Войдите по почте".
from auth_window_imports_options import *
from tests.test_13_authorisation.test_13_6_1_email_back import email_window_check
from tests.test_13_authorisation.test_13_4_cant_sign_in import cant_sign_in

# Открыть окно "Войдите по почте".
email_window_check()

# Запустить тестирование кнопки "Не могу войти".
cant_sign_in()
