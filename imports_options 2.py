# Импорт необходимых библиотек и модулей.

import time
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Настроить опции браузера.
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager"
chrome_options.add_argument("--window-size=1920,1280")
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3")
# Берем прокси айпи (например отсюда https://hidexy.name/proxy-list/)
# PROXY_SERVER = "46.254.92.206:80"
# chrome_options.add_argument(f"--proxy-server={PROXY_SERVER}")

# Инициализировать работу с драйвером.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Инициализировать синхронизацию загрузки страниц.
wait = WebDriverWait(driver, 5, poll_frequency=1)

# ФИКСТУРЫ ДЛЯ ФАЙЛА conftest.py

# @pytest.fixture(autouse=True) # Пока не обращаем внимания на эту строку
# def get_driver(request):
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     request.cls.driver = driver