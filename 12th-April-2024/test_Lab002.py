""" # Selenium
# Automates Browsers
import time

import pytest
from selenium import webdriver


@pytest.mark.normal
def test_open_vwlogin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(5)
    print(driver.title)
    assert driver.title == "Login - VWO"


    driver.quit() """

# Selenium
# Automates Browsers
# Selenium 3 - 20% on the Selenium 3 - Json wire protocol
# Selenium 4 - 70%+ (migrated to Selenium 4) ,W3C protocol, selenium manager

# pip install selenium -> 4.x -> you don't have to setup the browser drivers.

# Selenium 3

from selenium import webdriver


def test_open_website():
    pass
    # driver_path = '/Users/pramod/Downloads/edge/msedgedriver'
    # driver = webdriver.EdgeService(executable_path=driver_path)
    # driver.get("https://app.vwo.com")






