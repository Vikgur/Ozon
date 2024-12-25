# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation.test_close_window import close_window


def test_close_window():
    # Открыть окно "Войдите по почте".
    email_window_check()

    # Запустить тестирование кнопки "Х" закрытия окна авторизации.
    close_window()
