from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from lesson_28.core.pages.abstract_page import AbstractPage
from lesson_28.core.web_elements.button import Button
from lesson_28.core.web_elements.input_field import InputField


class SignUpAndLoginPage(AbstractPage):
    _driver: WebDriver

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def sign_up_name_field(self) -> InputField:
        return InputField(self._driver, (By.XPATH, ".//input[@name='name']"))

    @property
    def sign_up_email_address_field(self) -> InputField:
        return InputField(self._driver, (By.XPATH, ".//input[@data-qa='signup-email']"))

    @property
    def sign_up_button(self) -> Button:
        return Button(self._driver, (By.XPATH, " .//button[@data-qa='signup-button']"))

    def sign_up_with_credentials(self, name: str, email: str):
        self.sign_up_name_field.fill(name)
        self.sign_up_email_address_field.fill(email)

        self.sign_up_button.click()
