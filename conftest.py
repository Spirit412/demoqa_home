from typing import Any, Generator
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver() -> Generator[WebDriver, Any, None]:
    # Инициализация драйвера с опциями для headless режима
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    driver: WebDriver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
