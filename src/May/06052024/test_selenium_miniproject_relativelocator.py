# Selenium Mini Project #7 for Relative Locators


# https://codepen.io/AbdullahSajjad/full/LYGVRgK
# Switch Iframe - result
# Find the button click on it
# Find the input username
# Below element - error message
# Assert that error message.


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

def test_selenium_project7():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.maximize_window()

    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    # Find the input username

    username = driver.find_element(By.XPATH, "//input[@id='username']")
    error_message = driver.find_element((locate_with(By.TAG_NAME, "small")).below(username)).text
    assert error_message == "Username must be at least 3 characters"
    time.sleep(10)
    driver.quit()

