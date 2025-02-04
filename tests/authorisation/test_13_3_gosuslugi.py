# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *


@allure.description(
    "Ожидаемый результат: после клика на кнопку «Вход через Госуслуги» происходит переход на окно госуслуг."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-13.3", name="Тестирование входа через Госуслуги")
def test_gosuslugi():
    # Кликнуть на кнопку "Вход через Госуслуги".
    action.click(on_element=authorisation_window.GOSUSLUGI_BUTTON).perform()
    time.sleep(2)

    # Переключить драйвер на вторую вкладку с окном Госуслуг.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Проверить через assert переход на окно Госуслуг.
    assert (
        driver.title == "Портал государственных услуг Российской Федерации"
    ), "Переход на Госуслуги не осуществлен :-("

    # Проверить через print переход на на окно Госуслуг.
    if driver.title == "Портал государственных услуг Российской Федерации":
        print("Окно Госуслуг успешно открылось!")
    else:
        print("Переход на Госуслуги не осуществлен :-(")

    print("ТЕСТ ПРОЙДЕН УCПЕШНО!")

    driver.quit()
