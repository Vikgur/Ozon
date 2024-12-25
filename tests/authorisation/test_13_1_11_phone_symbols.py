# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field

@allure.description(
    "Ожидаемый результат: поле ввода не отображает вводимые символы, после клика на кнопку «Войти» появляется ошибка «Некорректный формат телефона» и окно ожидания отправленного смс кода не открывается."
)
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase(
    "Ozon-13.1.11", name="Ввести 10 символов  < > * ! @ # $ % & /"
)
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
