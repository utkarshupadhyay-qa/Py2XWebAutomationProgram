# Explicit Wait

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# Selenium TC4

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC #1: Simple Login Check on vwo.com website")

def test_vwologin_negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    # error_msg_element - comes after 5 seconds
    # I have to wait with some condition -
    # Wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # Conditions can be as follows:
    # pageTitle = vwo.com
    # Until error message is visible -> will not move forward
    # Until error msg is seen on the DOM (html) - i will not read the text

    # Explicit Wait
    # Telling WebDriver to wait for 5 seconds for visibility of this element
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))   # It takes tupples that's why (())
    )
    # Maximum duration WebDriver will wait is 5 seconds, if it finds element at 2 seconds,
    # then it will proceed to next command
    # t = 2

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()