from lesson_28.core.web_elements.abstract_element import AbstractElement
from selenium.webdriver.ie.webdriver import WebDriver


class Button(AbstractElement):

    def __init__(self, driver: WebDriver, locator: tuple[str, str]) -> None:
        super().__init__(driver, locator)

    def click(self) -> None:
        self.wait_to_be_clickable().click()
