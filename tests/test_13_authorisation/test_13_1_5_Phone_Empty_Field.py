# Импортировать опции драйвера и открыть окно авторизации.
from auth_window_imports_options import *
from Tests.test_13_Authorisation import validate_phone_field

# Создать функцию работы с пустым полем ввода номера телефона.
def valid_empty_steps():
    # Создать объект класса Validate для работы с проверками.
    validate = validate_phone_field.Validate()

    # Проверить, что поле ввода пустое.
    validate.valid_empty_input()

    # Кликнуть на кнопку "Войти".
    wait.until(EC.element_to_be_clickable(authorisation_window.LOGIN_BUTTON)).click()
    time.sleep(2)

    # Проверить появление ошибки «Некорректный формат телефона».
    validate.valid_error_input()

    # Проверить, что окно ожидания введения
    # отправленного смс кода не открылось.
    validate.sms_window_not_open()

if __name__ == '__main__':
    
    # Проверрить корректную работу с пустым полем ввода номера телефона.
    valid_empty_steps()
    
    driver.quit()

    # Через print вывести время, за которое тест был выполнен.
    # Результат округлить до сотых.
    print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
