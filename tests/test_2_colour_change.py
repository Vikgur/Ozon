import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.MainPage import MainPage


@allure.description(
    "Ожидаемый результат: при наведении на иконку «список заказов» цвет должен измениться."
)
@allure.tag("Главная страница")
@allure.label("Автор тест-кейса", "Виктор Гурко")
@allure.link("https://gitlab.com/Vikgur/ozon/", name="Тест-кейсы для Ozon")
@allure.testcase(
    "Ozon-2",
    name="Тестирование смены цвета иконки «список заказов» при наведении курсора",
)
def test_colour_change():
    # Создать объект класса ActionChains.
    action = ActionChains(driver)

    # Передать управление страницей драйверу.
    driver.get("https://www.ozon.ru/")
    time.sleep(5)

    # После запуска драйвера и открытия главной страницы
    # создать объект главной страницы класса main_page.
    main_page = MainPage(driver)

    # Создать объект до наведения мышки на элемент.
    before_move_to_element = main_page.MAIN_ORDER_LIST

    # Создать переменную для целочисленного
    # определения цвета до наведения на элемент.
    colour_before = int(
        "".join(
            i
            for i in before_move_to_element.value_of_css_property("color")
            if i.isdigit()
        )
    )
    time.sleep(2)

    # Через print вывести на экран цвет элемента до наведения мышки в rgba.
    print(
        f'Цвет до наведения мышки: {before_move_to_element.value_of_css_property("color")}'
    )

    action.move_to_element(before_move_to_element).perform()
    time.sleep(5)

    # Создать объект после наведения мышки на элемент.
    after_move_to_element = main_page.MAIN_ORDER_LIST

    # Создать переменную для целочисленного
    # определения цвета после наведения мышки на элемент.
    colour_after = int(
        "".join(
            i
            for i in before_move_to_element.value_of_css_property("color")
            if i.isdigit()
        )
    )

    # Через print вывести на экран цвет элемента до наведения мышки в rgba.
    print(
        f'Цвет после наведения мышки: {after_move_to_element.value_of_css_property("color")}'
    )

    # Проверить через assert изменения цвета элемента после наведения мышки.
    assert colour_before != colour_after, "Цвет букв остался прежним :-("

    # Проверить через print изменения цвета элемента после наведения мышки.
    if colour_before != colour_after:
        print("Цвет элемента изменился: ТЕСТ ПРОЙДЕН УСПЕШНО!")
    else:
        print("Цвет остался прежним :-(")

    driver.quit()
