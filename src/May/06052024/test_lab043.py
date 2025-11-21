import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *


def test_expcetion():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        textarea = driver.find_element(By.NAME, "q")
        # textarea is found
        driver.refresh()
        # After refresh DOM elements are refreshed
        # Webdriver is confused -> Stale Element Exception
        # // Refresh -> Navigate other Page, change in DOM elements (Ajax Calls) - VueJS, AngularJS
        # webdriver -> stale element exception

        # driver.switch_to.alert -> NoAlertPresentException
        # To fix Stale element Exception -> After refresh we have to again find the element
        textarea = driver.find_element(By.NAME, "q")
        textarea.send_keys("the testing academy")
    except StaleElementReferenceException as see:
        print(see)

    time.sleep(10)
    driver.quit()