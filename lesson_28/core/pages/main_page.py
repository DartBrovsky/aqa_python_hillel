from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from lesson_28.core.pages.abstract_page import AbstractPage
from lesson_28.core.pages.signup_and_login_page import SignUpAndLoginPage
from lesson_28.core.web_elements.button import Button


class MainPage(AbstractPage):
    _driver: WebDriver

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def signup_and_login_button(self) -> Button:
        return Button(self._driver, (By.XPATH, ".//li[./a[text()=' Signup / Login']]"))

    def go_to_signup_and_login_page(self) -> SignUpAndLoginPage:
        self.signup_and_login_button.click()

        return SignUpAndLoginPage(self._driver)
