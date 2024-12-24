import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.OzonTravel import OzonTravel
from page_elements.OzonTravelDates import OzonTravelDates
from page_elements.OzonTravelPassengers import OzonTravelPassengers

# Создать функцию заполнения всех полей.
def positive_fill():

    # Создать объект класса ActionChains.
    action = ActionChains(driver)

    # Передать управление страницей драйверу.
    driver.get("https://www.ozon.ru/travel/")
    time.sleep(5)

    # Cоздать объект страницы класса OzonTravel.
    ozon_page = OzonTravel(driver)

    # Очистить поле ввода "Откуда".
    wait.until(EC.element_to_be_clickable(ozon_page.INPUT_FROM_CLEAR)).click()
    time.sleep(2)

    # Ввести данные в поле "Откуда".
    ozon_page.INPUT_FROM.send_keys("Владивосток")
    time.sleep(2)

    # Кликнуть на "Владивосток" из выпадаюзщего списка.
    VLADIVOSTOK_LOCATOR = ("xpath", "//span[normalize-space(.)='Владивосток']")
    VLADIVOSTOK = driver.find_element(*VLADIVOSTOK_LOCATOR).click()
    time.sleep(2)

    # Кликнуть на поле "Куда".
    action.click(ozon_page.INPUT_TO).perform()
    time.sleep(1)
    action.click(ozon_page.INPUT_TO).perform()
    time.sleep(2)

    # Ввести данные в поле "Куда".
    ozon_page.INPUT_TO.send_keys("Москва")
    time.sleep(2)

    # Кликнуть на "Москва" из выпадающего списка.
    MOSCOW_LOCATOR = ("xpath", "//span[normalize-space(.)='Москва']")
    MOSCOW = driver.find_element(*MOSCOW_LOCATOR).click()
    time.sleep(2)

    # Кликнуть на опцию "Даты".
    action.click(ozon_page.INPUT_DATE).perform()
    time.sleep(1)
    action.click(ozon_page.INPUT_DATE).perform()
    time.sleep(2)

    # Создать объект выпадающей опции "Даты" класса OzonTravelDates.
    ozon_page_dates = OzonTravelDates(driver)

    # Выбрать месяц Март.
    action.click(ozon_page_dates.INPUT_DATE_MONTH_MARCH).perform()
    time.sleep(2)

    # Выбрать дату 1 Марта.
    action.click(ozon_page_dates.INPUT_DATE_DAY_1).perform()
    time.sleep(2)

    # Создать переменную локатора кнопки "Обратный билет не нужен".
    INPUT_DATE_ONE_WAY_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Обратный билет не нужен']",
    )

    # Создать переменную элемента кнопки "Обратный билет не нужен".
    INPUT_DATE_ONE_WAY = driver.find_element(*INPUT_DATE_ONE_WAY_LOCATOR)

    # Кликнуть на "Обратный билет не нужен".
    action.click(INPUT_DATE_ONE_WAY).perform()
    time.sleep(2)

    # Отключить уведомление о куках.
    COOKIE_LOCATOR = (
        "xpath",
        "//button[normalize-space(.)='ОК']",
    )
    COOKIE = driver.find_element(*COOKIE_LOCATOR).click()
    time.sleep(2)

    # Кликнуть на опцию "Пассажиры и класс".
    action.click(ozon_page.INPUT_PASSENGERS_CLASS).perform()
    time.sleep(2)

    # Создать объект выпадающей опции
    # "Пассажиры и класс" класса OzonTravelPassengers.
    ozon_page_passengers = OzonTravelPassengers(driver)

    # Добавить 1 пассажира ребенка "до 2 лет".
    action.click(ozon_page_passengers.INPUT_PASSENGERS_NEWBORN_ADD).perform()
    time.sleep(2)

    # Выбрать класс "Бизнес".
    action.click(ozon_page_passengers.INPUT_PASSENGERS_CLASS_BUSINESS).perform()
    time.sleep(2)

if __name__ == "__main__":
    
    # Создать переменную начала выполнения кода.
    start_time = time.time()
    
    # Заполнить все поля.
    positive_fill()

    # Создать объект класса ActionChains.
    action = ActionChains(driver)

    # После запуска драйвера создать объект
    # страницы класса OzonTravel.
    ozon_page = OzonTravel(driver)

    # Кликнуть на кнопку "Найти билеты".
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(1)
    action.click(ozon_page.FIND_TICKETS_BUTTON).perform()
    time.sleep(5)

    # Переключить драйвер на вторую вкладку с товаром.
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Создать переменные локатора и элемента кнопки "Показать график цен"
    # на открывшейся странице результатов поиска.
    SHOW_PRICE_CHART_LOCATOR = ("xpath", "//div[normalize-space(.)='Показать график цен']")
    SHOW_PRICE_CHART = driver.find_element(*SHOW_PRICE_CHART_LOCATOR)

    # Проверить через assert открытие страницы результатов поиска.
    assert (
    SHOW_PRICE_CHART.text == "Показать график цен"
    ), "Страница с результатами поиска не открылась :-("

    # Проверить через print открытие страницы результатов поиска.
    if SHOW_PRICE_CHART.text == "Показать график цен":
        print("Страница с результатами поиска открылась!")
    else:
        print("Страница с результатами поиска не открылась :-(")

    print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

    driver.quit()

    # Через print вывести время, за которое тест был выполнен.
    # Результат округлить до сотых.
    print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
