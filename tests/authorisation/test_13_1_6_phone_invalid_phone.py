# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


def test_invalid_phone():
    # Создать объект класса PhoneField.
    field = phone_field.PhoneField()

    # Ввести цифру 1111111111 в поле ввода номера телефона.
    authorisation_window.PHONE_INPUT_FIELD.send_keys(1111111111)
    time.sleep(2)

    # Проверить корректную работу с валидным ошибочным значением.
    field.valid_error_steps()

    print("ТЕСТ ПРОЙДЕН УПЕШНО!")

    driver.quit()