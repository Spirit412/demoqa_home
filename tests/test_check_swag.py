import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.swag_labs import SwagLabs


# @pytest.mark.parametrize("url", ["https://www.saucedemo.com/"])
def test_check_icon(driver: WebDriver) -> None:
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_icon()


# @pytest.mark.parametrize("url", ["https://www.saucedemo.com/"])
def test_check_username_field(driver: WebDriver):
    page = SwagLabs(driver)
    page.visit()
    assert page.find_element(locator="input#user-name")


# @pytest.mark.parametrize("url", ["https://www.saucedemo.com/"])
def test_check_password_field(driver: WebDriver):
    page = SwagLabs(driver)
    page.visit()
    assert page.find_element(locator="input#password")
