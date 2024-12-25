# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


def test_float_comma():
    # Создать объект класса PhoneField.
    field = phone_field.PhoneField()

    # Ввести цифру 9,999999999 в поле ввода номера телефона.
    authorisation_window.PHONE_INPUT_FIELD.send_keys("9,999999999")
    time.sleep(2)

    # Проверить корректную работу с валидным значением.
    field.valid_steps()

    print("ТЕСТ ПРОЙДЕН УПЕШНО!")

    driver.quit()
