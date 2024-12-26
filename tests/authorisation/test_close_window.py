# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *


# Создать функцию тестирования кнопки "Х" закрытия окна авторизации.
def close_window():

    # Переключить драйвер на основной html.
    driver.switch_to.default_content()

    # Создать переменную локатора кнопки закрытия окна "Х".
    CLOSE_WINDOW_LOCATOR = (
        "xpath",
        "//button[@class='b6025-b1 b6025-a7 ag022-a0 ag022-a5 ag022-a2']",
    )

    # Создать переменную элемента кнопки закрытия окна "Х".
    CLOSE_WINDOW = driver.find_element(*CLOSE_WINDOW_LOCATOR)

    # Кликнуть на кнопку акрытия окна "Х".
    wait.until(EC.element_to_be_clickable(CLOSE_WINDOW)).click()
    time.sleep(2)

    # Создать переменную локатора проверки
    # закрытия окно "Авторизация".
    IFRAME_LOCATOR = ("xpath", "//iframe")

    # Создать переменную проверки
    # перехода на окно "Выберите причину".
    IFRAME = driver.find_elements(*IFRAME_LOCATOR)

    # Проверить через assert переход на окно "Выберите причину".
    assert len(IFRAME) == 0, 'Окно "Авторизация" не закрылось :-('

    # Проверить через print переход на окно "Выберите причину".
    if len(IFRAME) == 0:
        print('Окно "Авторизация" успешно закрылось!')
    else:
        print('Окно "Авторизация" не закрылось :-(')

    print("ТЕСТ ПРОЙДЕН УCПЕШНО!")

    driver.quit()
