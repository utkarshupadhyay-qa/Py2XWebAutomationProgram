# Selenium Mini project #3
#
#
# Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
# Enter all the fields excepts the username
# Verify that the error message comes when you click on the submit button.


import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

def test_mini_project3():

    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")

    driver.maximize_window()

    # <input
    # type="text"
    # id="email"
    # placeholder="Enter email"
    # >

    time.sleep(10)

    iframe = driver.find_element(By.XPATH,"//iframe[@id='result']")

    driver.switch_to.frame(iframe)


    time.sleep(10)


    email = driver.find_element(By.XPATH, "//input[@id='email']")
    email.send_keys("abc_123@gmail.com")

    time.sleep(10)


    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("123456")

    time.sleep(10)

    confirm_password = driver.find_element(By.XPATH, "//input[@id='password2']")
    confirm_password.send_keys("123456")


    time.sleep(5)

    button = driver.find_element(By.XPATH,"//button[text()='Submit']")
    button.click()

    time.sleep(10)


    error_message = driver.find_element(By.XPATH,"//small[text()='Username must be at least 3 characters']")

    allure.attach(driver.get_screenshot_as_png(),name="Error Message Screenshot", attachment_type=AttachmentType.PNG)

    assert error_message.text == "Username must be at least 3 characters"

    time.sleep(10)


