# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import validate_phone_field


# Создать функцию работы поля с валидным значением
# в поле ввода номера телефона.
def valid_steps():

    # Создать объект класса Validate для работы с проверками.
    validate = validate_phone_field.Validate()

    # Проверить валидность введенных символов.
    validate.valid_input()

    # Кликнуть на кнопку "Войти".
    wait.until(EC.element_to_be_clickable(authorisation_window.LOGIN_BUTTON)).click()
    time.sleep(2)

    # Проверить открытие окна ожидания введения отправленного смс кода.
    validate.sms_window_open()


if __name__ == "__main__":

    # Ввести цифру 9999999999 в поле ввода номера телефона.
    authorisation_window.PHONE_INPUT_FIELD.send_keys("9999999999")
    time.sleep(2)

    # Проверить корректную работу с валидным значением.
    valid_steps()

    driver.quit()

