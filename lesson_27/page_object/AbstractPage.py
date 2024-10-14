from abc import ABC

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_27.web_elements.AbstractElement import AbstractElement


class AbstractPage(ABC):
    _driver: WebDriver
    _wrapped_element: AbstractElement

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wrapped_element = AbstractElement(self._driver)




