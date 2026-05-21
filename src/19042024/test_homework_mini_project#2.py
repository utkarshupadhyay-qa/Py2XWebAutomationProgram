# Selenium Mini Project #2

# Open the URL - https://www.idrive360.com/enterprise/login
# Enter the username, password
# Verify that Trial is finished and current URL also
# Add a logic to add Allure Screen for the Trail end.

# Username - augtest_040823@idrive.com
# password - 1234561

import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

def test_idrive360_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    # HTML Elements for username :
    # <input
    # _ngcontent-rfn-c171=""
    # type="email"
    # id="username"
    # name="username"
    # autofocus=""
    # class="id-form-ctrl ng-pristine ng-valid ng-touched"
    # >

    username_element = driver.find_element(By.ID , "username")
    username_element.send_keys("augtest_040823@idrive.com")

    # HTML Element for password:
    #<input
    # _ngcontent-rfn-c171=""
    # id="password"
    # name="password"
    # tabindex="0"
    # maxlength="20"
    # class="id-form-ctrl ng-untouched ng-pristine ng-valid"
    # type="password"
    # >

    time.sleep(5)

    password_element = driver.find_element(By.ID,"password")
    password_element.send_keys("1234561")

    time.sleep(5)


    # HTML element for Login button:
    # <button
    # _ngcontent-rfn-c171=""
    # type="submit"
    # id="frm-btn"
    # class="id-btn id-info-btn-frm"
    # >Sign in
    # </button
    # >

    signin_element = driver.find_element(By.ID , "frm-btn")
    signin_element.click()

    time.sleep(5)

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"

    # Html Element for Text :
    # <h5
    # _ngcontent-jdd-c141=""
    # class="id-card-title">
    # Your free trial has expired!
    # </h5>

    message_element = driver.find_element(By.CLASS_NAME,"id-card-title")
    print(message_element)

    assert message_element == "Your free trial has expired"

    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name="Free Trial expired screenshot", attachment_type=AttachmentType.PNG)

    driver.quit()


