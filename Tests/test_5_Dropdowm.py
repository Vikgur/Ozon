import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from Page_Elements.MainPage import MainPage
from Page_Elements.MainPageFaceIcon import MainPageFaceIcon
from Page_Elements.Allerts import Allerts
from Locators.locators import MainPageFaceIconLocators

# Создать опеременную начала выполнения кода.
start_time = time.time()

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

# После принятия куков создать объект
# главной страницы класса MainPage.
main_page = MainPage(driver)

# Навести мышку на иконку "лицо" в шапке.
action.move_to_element(main_page.MAIN_FACE_ICON).perform()
time.sleep(2)

# После наведения мышки на иконку "лицо"
# создать объект класса MainPageFaceIcon.
main_page_face_icon = MainPageFaceIcon(driver)

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

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
