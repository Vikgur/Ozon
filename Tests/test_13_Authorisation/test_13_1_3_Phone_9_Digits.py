# Импортировать опции драйвера и открыть окно авторизации.
from auth_window_imports_options import *
from Tests.test_13_Authorisation import validate_phone_field


# Создать функцию работы поля с валидным ошибочным
# значением в поле ввода номера телефона.
def valid_error_steps():

    # Создать объект класса Validate для работы с проверками.
    validate = validate_phone_field.Validate()

    # Проверить валидность введенных символов.
    validate.valid_input()

    # Кликнуть на кнопку "Войти".
    wait.until(EC.element_to_be_clickable(authorisation_window.LOGIN_BUTTON)).click()
    time.sleep(2)

    # Проверить, что окно ожидания введения
    # отправленного смс кода не открылось.
    validate.sms_window_not_open()


if __name__ == "__main__":

    # Ввести цифру 999999999 в поле ввода номера телефона.
    authorisation_window.PHONE_INPUT_FIELD.send_keys(999999999)
    time.sleep(2)

    # Проверить корректную работу с валидным ошибочным значением.
    valid_error_steps()

    driver.quit()

    # Через print вывести время, за которое тест был выполнен.
    # Результат округлить до сотых.
    print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
