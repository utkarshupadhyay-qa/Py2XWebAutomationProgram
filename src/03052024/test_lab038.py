# JavaScript Executor

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_01_JS1():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    # Javascript executor
    button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    # button.click()  - this is traditional way in selenium

    # But sometimes click doesn't work - so we need JavaScript Code to click on this button

    # Use the Javascript code to click on this button also
    js_ex = driver.execute_script
    js_ex("arguments[0].click()", button)  # On button element execute this code/script(arguments[0].click())
    js_ex("arguments[0].click()", button)
    # Clicking "add Element" button 2 times


    time.sleep(10)
    driver.quit()