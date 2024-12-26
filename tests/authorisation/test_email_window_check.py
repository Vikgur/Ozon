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
