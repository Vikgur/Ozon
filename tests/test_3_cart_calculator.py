import sys

sys.path.append(sys.path[0] + "/..")
from imports_options import *
from page_elements.CartPageProducts import CartPageTwoProducts
from main_detail_cart import MainDetailCart

# Создать переменную начала выполнения кода.
start_time = time.time()

# Создать объект для добавления с главной страницы
# 2 товаров в корзину класса MainDetailCart.
main_detail_cart = MainDetailCart()

# Добавить с главной страницы 2 товара в корзину
main_detail_cart.two_products()

# После переключения драйвера на третью вкладку
# создать объект страницы корзины CartPage.
cart_page = CartPageTwoProducts(driver)

# Создать переменную подсчета общей стоимости
# с Ozon Картой всех едининц первого товара.
sum_price_product_1 = int(
    "".join(i for i in cart_page.CART_PRODUCT_1_PRICE.text if i.isdigit())
)

# Создать переменную подсчета общей стоимости
# с Ozon Картой всех единиц второго товара.
sum_price_product_2 = int(
    "".join(i for i in cart_page.CART_PRODUCT_2_PRICE.text if i.isdigit())
)

# Создать переменную подсчета итоговой стоимости
# с Ozon Картой всех товаров в корзине.
total_price_in_cart = int(
    "".join(i for i in cart_page.CART_TOTAL_PRICE.text if i.isdigit())
)

# Проверить через assert сравнение суммы единиц
# первого и второго товара с итоговой суммой в корзине.
assert (
    sum_price_product_1 + sum_price_product_2 == total_price_in_cart
), "Итоговая сумма рассчитана не верно"

# Проверить через print сравнение суммы единиц
# первого и второго товара с итоговой суммой в корзине.
if sum_price_product_1 + sum_price_product_2 == total_price_in_cart:
    print(f"Cумма товаров равна итоговой сумме в корзине = {total_price_in_cart} Руб")
    print("ТЕСТ ПРОЙДЕН!")
else:
    print("Суммы не равны :-(")

driver.quit()

# Через print вывести время, за которое тест был выполнен.
# Результат округлить до сотых.
print("Тест выполнен за %s секунд" % round((time.time() - start_time), 2))
