# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from auth_window_imports_options import *
from Tests.test_13_Authorisation.test_13_6_1_Email_Back import email_window_check
from Tests.test_13_Authorisation.test_13_5_Сlose_Window import close_window

# Открыть окно "Войдите по почте".
email_window_check()

# Запустить тестирование кнопки "Х" закрытия окна авторизации.
close_window()
