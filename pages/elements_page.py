from pages.base_page import BasePage
from components.components import WebElement

class ElementsPage(BasePage):
    def __init__(self, driver) -> None:
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)
        self.text_center = WebElement(
            driver, "#app > div > div > div > div.col-12.mt-4.col-md-6"
        )

    def equal_url(self) -> bool:
        return self.get_url() == self.base_url
