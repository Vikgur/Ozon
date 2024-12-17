# Импортировать опции драйвера, открыть окно авторизации,
# открыть окно "Войдите по почте".
from auth_window_imports_options import *
from Page_Elements.MainPageAuthorisationEmailWindow import (
    MainPageAuthorisationEmailWindow,
)
from Tests.test_13_Authorisation.test_13_6_1_Email_Back import email_window_check

# Открыть окно "Войдите по почте".
email_window_check()

# Создать объект окна "Войдите по почте"
# класса MainPageAuthorisationEmailWindow.
email_window = MainPageAuthorisationEmailWindow(driver)

# Кликнуть на поле ввода и ввести данные.
(
action.click(email_window.INPUT_FIELD)
.pause(1)
.send_keys("йцукен23456789")
.perform()
)
time.sleep(2)

# Создать переменную локатора кнопки очистки поля ввода "х".
CLEAR_FIELD_LOCATOR = ("xpath", "//div[@class='f019-b a2019-a']")

# Создать переменную элемента кнопки очистки поля ввода "х".
CLEAR_FIELD = driver.find_element(*CLEAR_FIELD_LOCATOR)

# Кликнуть на кнопку очистки поля ввода "х".
wait.until(EC.element_to_be_clickable(CLEAR_FIELD)).click()
time.sleep(2)

# Проверить через assert, что поле ввода пустое.
assert len(driver.find_elements(*CLEAR_FIELD_LOCATOR)) == 0, "Поле ввода не пустое :-("

# Проверить через print, что поле ввода пустое.
if len(driver.find_elements(*CLEAR_FIELD_LOCATOR)) == 0:
    print("Поле ввода очистилось!")
else:
    print("Поле ввода не пустое :-(")

print("ТЕСТ ПРОЙДЕН УCПЕШНО!")

driver.quit()

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
