import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.MainPageAuthorisationIcon import MainPageAuthorisationIcon
from page_elements.Allerts import Allerts
from locators.locators import MainPageFaceIconLocators


@allure.description(
    "Ожидаемый результат: при наведение на «лицо» должен выпадать список кнопок: «Войти или зарегистрироваться» и «Личный кабинет». При клике на «Войти или зарегистрироваться» появляется модальное неблокирующее окно регистрации на текущей странице. При клике на «Личный кабинет» открывается страница личного кабинета."
)
@allure.tag("Главная страница")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase("Ozon-5", name="Тестирование выпадающих списков элементов")
def test_dropdown():
    # Создать объект класса ActionChains.
    action = ActionChains(driver)

    # Передать управление страницей драйверу.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # После запуска драйвера и открытия главной страницы
    # создать объект управления уведомлениями класса AllertsPage.
    allerts = Allerts(driver)

    # Отключить уведомления о куках.
    wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
    time.sleep(3)

    # После принятия куков создать объект класса MainPageAuthorisationIcon.
    main_page = MainPageAuthorisationIcon(driver)

    # Навести мышку на иконку "лицо" в шапке.
    action.move_to_element(main_page.MAIN_FACE_ICON).perform()
    time.sleep(2)

    # Создать переменную кнопки "Войти или зарегистрироваться"
    # для проверки ее наличия в выпадающем списке/меню.
    VISIBILITY_SIGN_IN_BUTTON = driver.find_elements(
        *MainPageFaceIconLocators.MAIN_FACE_ICON_SIGN_IN_LOCATOR
    )

    # Проверить через assert наличие кнопки
    # "Войти или зарегистрироваться" в выпадающем списке/меню.
    assert len(VISIBILITY_SIGN_IN_BUTTON) > 0, "Выпадающий список/меню не появился :-("

    # Проверить через print наличие кнопки
    # "Войти или зарегистрироваться" в выпадающем списке/меню.
    if len(VISIBILITY_SIGN_IN_BUTTON) > 0:
        print("Выпадающий список появился: ТЕСТ ПРОЙДЕН УСПЕШНО")
    else:
        print("Выпадающий список не выпал :-(")

    driver.quit()
