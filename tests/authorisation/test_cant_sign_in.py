# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *


# Создать функцию тестирования кнопки "Не могу войти".
def cant_sign_in():

    # Кликнуть на кнопку "Не могу войти".
    wait.until(EC.element_to_be_clickable(authorisation_window.CAN_NOT_SIGN_IN)).click()
    time.sleep(2)

    # Создать переменную локатора проверки
    # перехода на окно "Выберите причину".
    REASON_WHY_LOCATOR = ("xpath", "//div[normalize-space(.)='Выберите причину']")

    # Создать переменную проверки
    # перехода на окно "Выберите причину".
    REASON_WHY = driver.find_element(*REASON_WHY_LOCATOR)

    # Проверить через assert переход на окно "Выберите причину".
    assert (
        REASON_WHY.text == "Выберите причину"
    ), 'Переход на окно "Выберите причину" не осуществлен :-('

    # Проверить через print переход на окно "Выберите причину".
    if REASON_WHY.text == "Выберите причину":
        print('Окно "Выберите причину" успешно открылось!')
    else:
        print('Переход на окно "Выберите причину" не осуществлен :-(')

    print("ТЕСТ ПРОЙДЕН УCПЕШНО!")

    driver.quit()