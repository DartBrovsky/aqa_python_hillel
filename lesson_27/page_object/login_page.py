from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_27.page_object.AbstractPage import AbstractPage


class LogInPage(AbstractPage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    email_input_field_locator: tuple[str, str] = (By.XPATH, ".//div[./h2[text()='Login to your account']]//input[@type='email']")
    password_input_field_locator: tuple[str, str] = (By.XPATH, ".//div[./h2[text()='Login to your account']]//input[@type='password']")
    login_button_locator: tuple[str, str] = (By.XPATH, ".//button[@data-qa='login-button']")

    @property
    def email_input_field(self) -> WebElement:
        return self._wrapped_element.find_element(self.email_input_field_locator)

    @property
    def password_input_field(self) -> WebElement:
        return self._wrapped_element.find_element(self.password_input_field_locator)

    @property
    def login_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.login_button_locator)

    def fill_login_data(self):
        self.email_input_field.send_keys("serhii@com.com")
        self.password_input_field.send_keys("serhii")

        return self

    def click_on_log_in_button(self) -> None:
        self.login_button.click()
