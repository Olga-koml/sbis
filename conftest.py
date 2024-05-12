import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


# scope="function"  # запуск драйвера на каждую функцию
# scope="class" # запуск драйвера на каждый класс
@pytest.fixture(scope="class", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument('--headless')  # без визуального запуска браузера, для запуска тестов в CI docker
    prefs = {
        "download.default_directory": f"{os.getcwd()}\\download_data",
        "safebrowsing.enabled": "false"     # чтоб браузер не блокировал загрузку
    }
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
