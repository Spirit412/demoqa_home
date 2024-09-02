from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement

class SwagLabs(BasePage):

    def __init__(self, driver) -> None:
        self.base_url = "https://www.saucedemo.com/"
        super().__init__(driver, self.base_url)

        self.text_footer = WebElement(driver, '#app > footer > span')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')

    def exist_icon(self) -> bool:
        try:
            self.find_element(locator="div.login_logo")
        except NoSuchElementException:
            return False
        return True

    def equal_url(self) -> bool:
        return self.get_url() == self.base_url
