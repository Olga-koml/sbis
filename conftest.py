import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# scope="function"  # запуск драйвера на каждую функцию
# scope="class" # запуск драйвера на каждый класс
@pytest.fixture(scope="class", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument('--headless') # для запуска тестов в CI docker
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
