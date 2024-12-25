# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


def test_symbols():
    # Создать объект класса PhoneField.
    field = phone_field.PhoneField()

    # Ввести "< > * ! @ # $ % & /" в поле ввода номера телефона.
    authorisation_window.PHONE_INPUT_FIELD.send_keys("< > * ! @ # $ % & /")
    time.sleep(2)

    # Проверрить корректную работу с пустым полем ввода номера телефона.
    field.valid_empty_steps()

    print("ТЕСТ ПРОЙДЕН УПЕШНО!")

    driver.quit()
