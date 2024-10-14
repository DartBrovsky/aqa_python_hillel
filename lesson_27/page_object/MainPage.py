from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from lesson_27.page_object.AbstractPage import AbstractPage
from lesson_27.page_object.login_page import LogInPage
from lesson_27.web_elements import AbstractElement


class MainPage(AbstractPage):

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    login_button_locator: tuple[str, str] = (By.XPATH, ".//li[./a[text()=' Signup / Login']]")
    logged_in_attributes_locator: tuple[str, str] = (By.XPATH, ".//li[./a[text()=' Logout' or text()=' Logged in as ']]")

    @property
    def login_button(self) -> WebElement:
        return self._wrapped_element.find_element(self.login_button_locator)

    @property
    def logged_in_attributes(self) -> list[WebElement]:
        return self._wrapped_element.find_elements(self.logged_in_attributes_locator)

    def go_to_login_page(self) -> LogInPage:
        self._wrapped_element.wait_to_be_clickable(self.login_button)
        self.login_button.click()

        return LogInPage(self._driver)

    def verify_that_user_is_logged_in(self):
        assert_that(len(self.logged_in_attributes) == 2).is_true()
        assert_that(all([element.is_displayed() for element in self.logged_in_attributes])).is_true()



