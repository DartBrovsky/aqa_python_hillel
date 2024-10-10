import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from lesson_26.conftest import web_driver_creation


# @pytest.mark.usefixtures("")
class TestInitialUiAutomation:
    BASE_URL: str = "https://www.automationexercise.com"

    def test_that_we_open_main_page(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)

        logo_section: WebElement = web_driver_creation.find_element(By.XPATH, ".//div[./a/img[@alt='Website for automation practice']]")

        brands_elements_list: list[WebElement] = web_driver_creation.find_elements(By.XPATH, ".//div[./h2[text()='Brands']]//li[./a]")

        assert_that(logo_section.is_displayed()).is_true()

        assert_that(len(brands_elements_list) == 8).is_true()

        assert_that(all([element.is_displayed() for element in brands_elements_list])).is_true()

    def test_log_in(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)

        sing_up_login_button: WebElement = web_driver_creation.find_element(By.XPATH, ".//ul[contains(@class, 'navbar')]/li[./a[contains(text(), 'Login')]]")
        sing_up_login_button.click()

        email_input_field: WebElement = web_driver_creation.find_element(By.XPATH, ".//div[./h2[text()='Login to your account']]//input[@type='email']")
        password_input_field: WebElement = web_driver_creation.find_element(By.XPATH, ".//div[./h2[text()='Login to your account']]//input[@type='password']")

        login_button: WebElement = web_driver_creation.find_element(By.XPATH, ".//button[@data-qa='login-button']")

        email_input_field.send_keys("serhii@gmail.com")
        password_input_field.send_keys("serhii")

        login_button.click()

        logged_in_attributes: list[WebElement] = web_driver_creation.find_elements(By.XPATH, ".//li[./a[text()=' Logout' or text()=' Logged in as ']]")

        assert_that(len(logged_in_attributes) == 2).is_true()
        assert_that(all([element.is_displayed() for element in logged_in_attributes])).is_true()

        time.sleep(5)

    def test_that_user_can_scroll_to_desired_element(self, web_driver_creation):
        web_driver_creation.get(self.BASE_URL)

        subscription_bottom_text_element: WebElement = web_driver_creation.find_element(By.XPATH, ".//h2[text()='Subscription']")

        web_driver_creation.execute_script("return arguments[0].scrollIntoView(true);", subscription_bottom_text_element)

        time.sleep(3)

    def test_that_user_can_add_item_into_cart(self, web_driver_creation):
        web_driver_creation.get("http://localhost:8000/dialog.html")

        time.sleep(5)

        web_driver_creation.find_element(By.XPATH, "//button[text()='Показати Alert']").click()
        alert = Alert(web_driver_creation)
        time.sleep(2)
        alert.accept()
        time.sleep(2)

        web_driver_creation.find_element(By.XPATH, "//button[text()='Показати Confirm']").click()
        alert = Alert(web_driver_creation)
        time.sleep(2)
        alert.accept()
        time.sleep(2)

        web_driver_creation.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
        alert = Alert(web_driver_creation)
        time.sleep(2)
        alert.send_keys("John")
        time.sleep(2)
        alert.accept()
        time.sleep(2)

    def test_that_user_can_perform_complex_actions(self, web_driver_creation):
        web_driver_creation.get("http://localhost:8000/action_chains.html")

        time.sleep(2)


