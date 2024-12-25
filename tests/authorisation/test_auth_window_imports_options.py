import sys

sys.path.append(sys.path[0] + "/../..")
from imports_options import *
from page_elements.MainPageAuthorisationIcon import MainPageAuthorisationIcon
from page_elements.MainPageAuthorisationWindow import (
    MainPageAuthorisationWindow,
    MainPageAuthorisationWindowLocators,
)
from tests.test_1_smoke import authorisation_page_check


# Создать объект класса ActionChains.
action = ActionChains(driver)

# Передать управление страницей драйверу.
driver.get("https://www.ozon.ru/")
time.sleep(5)

# После запуска драйвера и открытия главной страницы
# создать объект главной страницы класса MainPageAuthorisationIcon.
main_page = MainPageAuthorisationIcon(driver)

# Кликнуть на иконку "Лицо" в шапке.
wait.until(EC.element_to_be_clickable(main_page.MAIN_FACE_ICON)).click()
time.sleep(2)

# Проверить, что окно авторизации открылось.
authorisation_page_check()

# Создать объект окна авторизации класса MainPageAuthorisationWindow.
authorisation_window = MainPageAuthorisationWindow(driver)
