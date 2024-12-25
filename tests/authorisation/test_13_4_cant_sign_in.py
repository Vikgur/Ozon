import allure
from tests.authorisation.test_cant_sign_in import cant_sign_in


@allure.description(
    "Ожидаемый результат: после клика на кнопку «Не могу войти» происходит переход на окно «Выберите причину»."
)
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-13.4", name="Тестирование кнопки «Не могу войти»")
def test_cant_sign_in():

    # Запустить тестирование кнопки "Не могу войти".
    cant_sign_in()
