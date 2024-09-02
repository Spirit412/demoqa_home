from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, locator="") -> None:
        self.locator = locator
        self.driver = driver

    def find_element(self):
        """Найти один элемент по локатору"""
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)
    
    def get_text(self):
        """Возвращает текст элемента.
        1. в классе компонентов создайте метод для получения текста с элементов get_text(self).
        текст из элемента считывайте так str(self.find_element().text)
        """
        return str(self.find_element().text)

    def exist(self):

        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True
    
    def click(self) -> None:
        """Кликнуть по элементу"""
        self.find_element().click()
