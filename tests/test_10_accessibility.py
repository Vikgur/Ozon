import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from scrolls import Scrolls
from page_elements.MainPageBottom import MainPageBottom
from page_elements.Allerts import Allerts
from locators.locators import AccessibilityPageLocators

# Создать переменную начала выполнения кода.
start_time = time.time()

# Создать объект класса ActionChains.
action = ActionChains(driver)

# Создать объект класса Scrolls.
scrolls = Scrolls(driver, action)

# Передать управление страницей драйверу.
driver.get("https://www.ozon.ru/")
time.sleep(5)

# Создать объект управления уведомлениями класса AllertsPage.
allerts = Allerts(driver)

# Отключить уведомления о куках.
wait.until(EC.element_to_be_clickable(allerts.ACCEPT_ALLERT_COOKIE)).click()
time.sleep(2)

# Скроллить в самый низ страницы к подвалу.
scrolls.scroll_to_bottom()
time.sleep(2)

# Скроллить в самый низ страницы к подвалу.
# Двойной скролл необходим в случае, если страница не успела прогрузиться.
scrolls.scroll_to_bottom()
time.sleep(2)

# Создать объект подвала главной страницы класса MainPageBottom.
main_page_bottom = MainPageBottom(driver)

# Кликнуть на кнопку "Для слабовидящих".
wait.until(EC.element_to_be_clickable(main_page_bottom.MAIN_ACCESSIBILITY)).click()
time.sleep(3)

# Создать переменную для проверки наличия локатора
# опции изменения шрифта на странице для слабовидящих.
VISIBILITY_FONT_OPTIONS = driver.find_elements(
    *AccessibilityPageLocators.VISIBILITY_FONT_CHANGE_OPTIONS_LOCATOR
)

# Проверить через assert открытие страницы для слабовидящих.
assert len(VISIBILITY_FONT_OPTIONS) > 0, "Страница для слабовидящих не открылась :-("

# Проверить через print открытие страницы для слабовидящих.
if len(VISIBILITY_FONT_OPTIONS) > 0:
    print("Страница для слабовидящих открылась! ТЕСТ ВЫПОЛНЕН УСПЕШНО!")
else:
    print("Страница для слабовидящих не открылась :-(")

driver.quit()

print("ТЕСТ ПРОЙДЕН УСПЕШНО!")

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
