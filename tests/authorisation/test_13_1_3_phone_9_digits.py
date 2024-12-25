# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Ожидаемый результат: поле отображает вводимые символы, после клика на кнопку «Войти» появляется ошибка «Некорректный формат телефона» и окно ожидания отправленного смс кода не открывается."
)
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-13.1.3", name="Ввести 9 чисел «999999999»")
def test_9_digits():
    # Создать объект класса PhoneField.
    field = phone_field.PhoneField()

    # Ввести цифру 999999999 в поле ввода номера телефона.
    authorisation_window.PHONE_INPUT_FIELD.send_keys(999999999)
    time.sleep(2)

    # Проверить корректную работу с валидным ошибочным значением.
    field.valid_error_steps()

    print("ТЕСТ ПРОЙДЕН УПЕШНО!")

    driver.quit()
