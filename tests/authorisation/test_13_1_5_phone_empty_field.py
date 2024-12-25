# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


def test_empty_field():
    # Создать объект класса PhoneField.
    field = phone_field.PhoneField()

    # Проверрить корректную работу с пустым полем ввода номера телефона.
    field.valid_empty_steps()
    
    print("ТЕСТ ПРОЙДЕН УПЕШНО!")
    
    driver.quit()

