from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


def element_is_not_here(driver, xpath):
    try:
        element = WebDriverWait(driver, timeout=5).until_not(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return True
    except TimeoutException:
        print("Елемент продовжує бути на сторінці після очікуваного часу")
        return False