import allure
from tests.authorisation.test_close_window import close_window

@allure.description(
    "Ожидаемый результат: после клика на кнопку «Х» в правом верхнем углу происходит закрытие окна авторизации."
)
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase(
    "Ozon-13.5", name="Тестирование кнопки закрытия окна «X»"
)
def test_close_window():
    # Запустить тестирование кнопки "Х" закрытия окна авторизации.
    close_window()
