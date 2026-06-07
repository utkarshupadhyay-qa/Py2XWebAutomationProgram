# Exceptions

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from selenium.common.exceptions import  *


def test_exception_1():
    driver = webdriver.Chrome()
    driver.get("https://google.com")

    #driver.find_element(By.NAME, "q").send_keys("the testing academy")

    # What if NAME value changed
    try:
        driver.find_element(By.NAME, "utkarsh").send_keys("the testing academy")
    except NoSuchElementException as nse:
        print(f"No such element found, please check locator: {nse}")

    time.sleep(10)
    driver.quit()