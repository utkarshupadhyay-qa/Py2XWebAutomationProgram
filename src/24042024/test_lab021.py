# Implicit Wait

import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium TC4

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC #1: Simple Login Check on vwo.com website")

def test_vwologin_negative():
    driver = webdriver.Chrome()
    # driver.implicitly_wait(5) - Webdriver to wait for all the elements
    # time.sleep(5) - time.sleep(15) #-> Thread.sleep() , Python Interpreter  wait.
    driver.get("https://app.vwo.com")

    # e1, e2 , e3 -> 3 elements
    # Tell Webdriver to wait for the 5 secs to Load for all 3 elements
    # Condition for all the elements.
    # What if the e1,e2,e3 loads in less than 3 secs, then 2 secs wasted.

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    # Python - Interpreter - It is super bad practice - time.sleep(5) - Worst type of Wait.
    # Webdriver

    time.sleep(5)  # This is Python Int who is waiting, Python Execution Halt.
                   # Instead Selenium Waits are better - because Webdriver will get halt not Python Interpreter

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
