import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chromium.options import ChromiumOptions

from lesson_28.core.test_data.test_data import TestData


@pytest.fixture(scope="class")
def web_driver():
    chrome_options: ChromiumOptions = webdriver.ChromeOptions()
    # Set up the desired capabilities for Chrome
    # chrome_options.browser_version = "100.0"
    # capabilities = DesiredCapabilities.CHROME.copy()
    # capabilities["browserName"] = "chrome"
    # capabilities["version"] = "100.0"
    # driver: WebDriver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=chrome_options)
    driver: WebDriver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(TestData.BASE_URL)

    yield driver

    driver.quit()
