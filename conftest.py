import pytest
from selenium import webdriver
from datetime import datetime, timedelta


@pytest.fixture
def setup_driver():
    """
    Инициализация веб-драйвера перед тестом.
    Закрытие веб-драйвера после выполнения теста.
    """
    driver = webdriver.Firefox()  # Вы можете заменить на другой драйвер
    driver.maximize_window()
    driver.get("https://example.com")  # Замените на ваш URL
    yield driver
    driver.quit()

@pytest.fixture
def tomorrow_date():
    tomorrow = datetime.now() + timedelta(days=1)
    return tomorrow.strftime("%d.%m.%Y")

