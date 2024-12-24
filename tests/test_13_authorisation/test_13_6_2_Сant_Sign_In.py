# Импортировать опции драйвера, открыть окно авторизации, 
# открыть окно "Войдите по почте".
from auth_window_imports_options import *
from Tests.test_13_Authorisation.test_13_6_1_Email_Back import email_window_check
from Tests.test_13_Authorisation.test_13_4_Сant_Sign_In import cant_sign_in

# Открыть окно "Войдите по почте".
email_window_check()

# Запустить тестирование кнопки "Не могу войти".
cant_sign_in()
