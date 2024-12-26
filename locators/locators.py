# Локатор иконки "Авторизация" главной страницы
class MainPageAuthorisationIconLocators(object):
    MAIN_FACE_ICON_LOCATOR = ("xpath", "//div[@data-widget='profileMenuAnonymous']")


# Локаторы шапки и главной страницы.
class MainPageLocators(MainPageAuthorisationIconLocators):
    def __init__(self):
        super().__init__(self)

    MAIN_SEARCH_LOCATOR = ("xpath", "//input[@type='text']")
    MAIN_FIRST_CATEGORY_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Товары нарасхват']",
    )
    MAIN_PRODUCT_1_LOCATOR = ("xpath", "(//div[@class='s4i_23'])[1]")
    MAIN_PRODUCT_2_LOCATOR = ("xpath", "(//div[@class='s4i_23'])[2]")
    MAIN_CURRENCY_LOCATOR = ("xpath", "//button[@data-widget='selectedCurrency']")
    MAIN_ORDER_LIST_LOCATOR = ("xpath", "//a[@href='/my/orderlist']")


# Локаторы подвала главной страницы.
class MainPageBottomLocators(object):
    MAIN_ACCESSIBILITY_LOCATOR = ("xpath", "//button[@class='b2121-a0 b2121-a4']")


# Локаторы главной страницы модального окна "Валюта".
class MainPageCurrencyLocators(object):
    MAIN_CURRENCY_VISIBILITY_LOCATOR = ("xpath", "//span[normalize-space(.)='Валюта']")
    MAIN_CURRENCY_DROPDOWN_LOCATOR = ("xpath", "//input[@title='Российский рубль']")


# Локаторы главной страницы модального окна "Валюта".
class MainPageCurrencyDropdownLocators(object):
    MAIN_CURRENCY_DROPDOWN_USD_LOCATOR = ("xpath", "//div[@title='Доллар США']")


# Локаторы главной страницы иконки "лицо" с выпадающим списком.
class MainPageFaceIconLocators(object):
    MAIN_FACE_ICON_LOCATOR = ("xpath", "//div[@data-widget='profileMenuAnonymous']")
    MAIN_FACE_ICON_SIGN_IN_LOCATOR = (
        "xpath",
        "//button[normalize-space(.)='Войти или зарегистрироваться']",
    )
    MAIN_FACE_ICON_ACCOUNT_LOCATOR = (
        "xpath",
        "//button[normalize-space(.)='Личный кабинет']",
    )


# Локаторы страницы деталировки (страница товара).
class DetailPageLocators(object):
    ADD_TO_CART_ICON_LOCATOR = ("xpath", "//a[@href='/cart']")


# Локаторы страницы деталировки c кнопкой "Купить в 1 клик".
class DetailPageBuyOneClickLocators(DetailPageLocators):
    def __init__(self):
        super().__init__(self)

    BUY_1_CLICK_LOCATOR = (
        "xpath",
        "//button[@data-widget='webOneClickButton']",
    )


# Локаторы страницы деталировки с множественным выбором единиц товара.
class DetailPageInDemandLocators(DetailPageLocators):
    def __init__(self):
        super().__init__(self)

    PRODUCT_ADD_LOCATOR = (
        "xpath",
        "(//button[@style='background:rgba(0, 162, 255, 1);color:rgba(245, 247, 250, 1);'])[1]",
    )


# Локаторы страницы деталировки с единичным выбором товара.
class DetailPageProductLocators(DetailPageLocators):
    def __init__(self):
        super().__init__(self)

    PRODUCT_ADD_TO_CART_LOCATOR = (
        "xpath",
        "(//button[@class='jy8_27 b2121-a0 b2121-b2 b2121-a4'])[2]",
    )
    GO_TO_DESCRIPTION_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Перейти к описанию']",
    )


# Локаторы страницы корзины с одним наименованием товара в корзине.
class CartPageOneProductLocators(object):
    CART_INPUT_PRODUCTS_1_LOCATOR = ("xpath", "(//input[@inputmode='numeric'])[1]")
    CART_PRODUCT_1_PRICE_LOCATOR = (
        "xpath",
        "//span[@class='c3023-a1 tsHeadline400Small c3023-b1 c3023-a5']",
    )
    CART_TOTAL_PRICE_LOCATOR = ("xpath", "//font[@color='#10C44C']")
    SHARE_BUTTON_LOCATOR = ("xpath", "(//div[@class])[69]")
    CLICK_TO_BUY_LOCATOR = (
        "xpath",
        "//button[normalize-space(.)='Перейти к оформлению']",
    )
    DELETE_ALL_SELECTED_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Удалить выбранные']",
    )


# Локаторы страницы корзины с двумя наименованиями товаров в корзине.
class CartPageTwoProductLocators(CartPageOneProductLocators):
    def __init__(self):
        super().__init__(self)

    CART_INPUT_PRODUCTS_2_LOCATOR = ("xpath", "(//input[@inputmode='numeric'])[2]")
    CART_PRODUCT_2_PRICE_LOCATOR = (
        "xpath",
        "(//span[@class='c3023-a1 tsHeadline400Small c3023-b1 c3023-a5'])[2]",
    )


# Локаторы страницы корзины - подтверждение удаления товара.
class CartPageDeleteConfirmLocators(object):
    DELETE_CONFIRM_LOCATOR = ("xpath", "//button[normalize-space(.)='Удалить']")


# Локаторы страницы авторизации.
class AuthorisationPageLocators(object):
    EMAIL_SIGN_IN_LOCATOR = ("xpath", "//button[normalize-space(.)='Войти по почте']")
    VISIBILITY_TEXT_PHONE_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Введите номер телефона']",
    )


# Локаторы всплывающих уведомлений.
class AllertsLocators(object):
    ACCEPT_ALLERT_COOKIE_LOCATOR = ("xpath", "//button[normalize-space(.)='ОК']")
    VISIBILITY_ALLERT_COOKIE_LOCATOR = ("xpath", "//button[normalize-space(.)='ОК']")


# Локаторы страницы для слабовидящих уведомлений.
class AccessibilityPageLocators(object):
    VISIBILITY_FONT_CHANGE_OPTIONS_LOCATOR = (
        "xpath",
        "//section[@id='accessibility-desk']",
    )


# Локаторы страницы каталога.
class CatalogPageCleanerLocators(object):
    ROBOT_CLEANER_FIRST_RESULT_LOCATOR = ("xpath", "(//div[@class='xi2_23'])[1]")
    FILTER_ROBOT_CLEANER_LOCATOR = (
        "xpath",
        "//a[normalize-space(.)='Роботы-пылесосы']",
    )
    FILTER_DELIVERY_TIME_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Сроки доставки']",
    )
    FILTER_DELIVERY_TIME_3_DAYS_CHECK_LOCATOR = (
        "xpath",
        "(//input[@class='c4014-a0'])[5]",
    )
    FILTER_DELIVERY_TIME_3_DAYS_CLICK_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='До 3 дней']",
    )
    FILTER_BRAND_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Бренд']",
    )
    FILTER_BRAND_XIAOMI_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Xiaomi']",
    )
    FILTER_PRICE_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Цена']",
    )
    FILTER_PRICE_INPUT_FROM_LOCATOR = (
        "xpath",
        "(//input[@type='text'])[2]",
    )
    FILTER_PRICE_INPUT_TO_LOCATOR = (
        "xpath",
        "(//input[@type='text'])[3]",
    )
    FILTER_ORIGINAL_LOCATOR = (
        "xpath",
        "(//input[@class='c7014-a0'])[3]",
    )
    FILTER_DUST_COLLECTOR_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Вид пылесборника']",
    )
    FILTER_DUST_CHECKBOX_CONTAINER_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Контейнер']",
    )
    FILTER_DUST_CHECKBOX_AQUA_LOCATOR = (
        "xpath",
        "//span[normalize-space(.)='Аквафильтр']",
    )
    SORTED_LOCATOR = (
        "xpath",
        "//input[@class='c1410-a7 tsBody500Medium c1410-a9']",
    )


# Локаторы окна "Авторизация".
class MainPageAuthorisationWindowLocators(object):
    CODE_LIST_LOCATOR = ("xpath", "//input[@readonly='readonly']")
    PHONE_INPUT_FIELD_LOCATOR = ("xpath", "//input[@type='tel']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//button[normalize-space(.)='Войти']")
    PHONE_INPUT_CHECK_LOCATOR = ("xpath", "//p[normalize-space(.)='999 999 99 99']")
    GOSUSLUGI_BUTTON_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Вход через Госуслуги']",
    )
    CAN_NOT_SIGN_IN_LOCATOR = (
        "xpath",
        "//button[normalize-space(.)='Не могу войти']",
    )
    EMAIL_SIGN_IN_LOCATOR = (
        "xpath",
        "//button[normalize-space(.)='Войти по почте']",
    )


# Локаторы окна "Войдите по почте".
class MainPageAuthorisationEmailWindowLocators(object):
    EMAIL_WINDOW_LOCATOR = ("xpath", "//div[normalize-space(.)='Войдите по почте']")
    BACK_TO_AUTHORISATION_WINDOW_LOCATOR = (
        "xpath",
        "//button[normalize-space(.)='Вернуться на главный экран']",
    )
    INPUT_FIELD_LOCATOR = ("xpath", "//input[@type='email']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//button[normalize-space(.)='Войти']")
    INPUT_PASSENGERS_CLASS_LOCATOR = ("xpath", "(//input[@type='text'])[4]")


# Локаторы Ozon Travel.
class OzonTravelLocators(object):
    INPUT_FROM_CLEAR_LOCATOR = ("xpath", "(//div[@class='a3pb_39'])[1]")
    INPUT_FROM_LOCATOR = ("xpath", "(//input[@type='text'])[1]")
    INPUT_TO_LOCATOR = ("xpath", "(//input[@type='text'])[2]")
    INPUT_DATE_LOCATOR = ("xpath", "(//input[@type='text'])[3]")
    INPUT_PASSENGERS_CLASS_LOCATOR = ("xpath", "(//input[@type='text'])[4]")
    FIND_TICKETS_BUTTON_LOCATOR = (
        "xpath",
        "//button[@class='apb4_39 ap4b_39 b2121-a0 b2121-b5 b2121-b2']",
    )


# Локаторы Ozon Travel поля "Даты".
class OzonTravelDatesLocators(OzonTravelLocators):
    def __init__(self):
        super().__init__(self)

    INPUT_DATE_DAY_LOCATOR = (
        "xpath",
        "(//div[@class='d4019-a ba2h_39' and normalize-space(.)='27'])[2]",
    )


# Локаторы Ozon Travel поля "Пассажиры и класс".
class OzonTravelPassengersLocators(OzonTravelLocators):
    def __init__(self):
        super().__init__(self)

    INPUT_PASSENGERS_NEWBORN_ADD_LOCATOR = (
        "xpath",
        "(//button[@class='ag022-a0 ag022-a7 ag022-a2'])[3]",
    )
    INPUT_PASSENGERS_CLASS_BUSINESS_LOCATOR = (
        "xpath",
        "//div[normalize-space(.)='Бизнес']",
    )
