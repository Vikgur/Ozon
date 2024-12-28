# Импортировать опции драйвера, открыть окно авторизации.
# открыть окно "Войдите по почте".
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation.test_email_window_check import email_window_check
from tests.authorisation.test_cant_sign_in import cant_sign_in


@allure.description(
    "Ожидаемый результат: после клика на кнопку «Не могу войти» происходит переход на окно «Выберите причину»."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-13.6.2", name="Тестирование кнопки «Не могу войти»")
def test_cant_sign_in():
    # Открыть окно "Войдите по почте".
    email_window_check()

    # Запустить тестирование кнопки "Не могу войти".
    cant_sign_in()
