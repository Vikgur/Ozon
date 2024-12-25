# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from tests.authorisation import phone_field


@allure.description(
    "Ожидаемый результат: после клика на кнопку «Войти» появляется ошибка «Некорректный формат телефона» и окно ожидания отправленного смс кода не открывается."
)
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-13.1.5", name="Оставить поле пустым")
def test_empty_field():
    # Создать объект класса PhoneField.
    field = phone_field.PhoneField()

    # Проверрить корректную работу с пустым полем ввода номера телефона.
    field.valid_empty_steps()

    print("ТЕСТ ПРОЙДЕН УПЕШНО!")

    driver.quit()
