# Импортировать опции драйвера и открыть окно авторизации.
from tests.authorisation.test_auth_window_imports_options import *
from page_elements.AuthorisationPage import AuthorisationPage
from page_elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)


# Создать функцию проверки, что открыто окно "Войдите по почте".
def email_window_check():

    # Кликнуть на кнопку "Войти по почте".
    wait.until(EC.element_to_be_clickable(authorisation_window.EMAIL_SIGN_IN)).click()
    time.sleep(2)

    # Создать объект окна "Войдите по почте"
    # класса MainPageAuthorisationEmailWindow.
    email_window = MainPageAuthorisationEmailWindow(driver)

    # Проверить через assert переход на окно "Войдите по почте".
    assert (
        email_window.EMAIL_WINDOW.text == "Войдите по почте"
    ), 'Переход на окно "Войдите по почте" не осуществлен :-('

    # Проверить через print переход на окно "Войдите по почте".
    if email_window.EMAIL_WINDOW.text == "Войдите по почте":
        print('Окно "Войдите по почте" открыто!')
    else:
        print('Окно "Войдите по почте" не открыта :-(')


if __name__ == "__main__":

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

