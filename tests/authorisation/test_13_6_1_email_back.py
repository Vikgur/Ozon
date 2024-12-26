# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.AuthorisationPage import AuthorisationPage
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from tests.authorisation.test_email_window_check import email_window_check


@allure.description(
    "Ожидаемый результат: после клика на кнопку «Вернуться на главный экран» происходит переход на шаг назад на окно авторизации."
)
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-13.6.1", name="Тестирование кнопки «Вернуться на главный экран»")
def test_email_back():
    # Открыть окно "Войдите по почте".
    email_window_check()

    # Создать объект окна "Войдите по почте"
    # класса MainPageAuthorisationEmailWindow.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Кликнуть на кнопку "Вернуться на главный экран".
    wait.until(
        EC.element_to_be_clickable(email_window.BACK_TO_AUTHORISATION_WINDOW)
    ).click()
    time.sleep(2)

    # После перехода на страницу авторизации
    # создать объект страницы авторизации класса AuthorisationPage.
    authorisation_page = AuthorisationPage(driver)

    # Проверить через assert переход на страницу авторизации.
    assert (
        authorisation_page.VISIBILITY_TEXT_PHONE.text == "Введите номер телефона"
    ), 'Переход обратно на окно "Введите номер телефона" не произошел :-('

    # Проверить через print переход на страницу авторизации.
    if authorisation_page.VISIBILITY_TEXT_PHONE.text == "Введите номер телефона":
        print('Переход обратно на окно "Введите номер телефона" произошел!')
    else:
        print('Переход обратно на окно "Введите номер телефона" не произошел :-(')

    print("ТЕСТ ПРОЙДЕН УCПЕШНО!")

    driver.quit()
