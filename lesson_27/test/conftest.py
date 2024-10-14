import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def create_driver():
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.automationexercise.com")

    return driver
