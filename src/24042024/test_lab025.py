import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)


# Selenium 4 - TC

@pytest.mark.smoke
@allure.title("Verify that Login is working in app.vwo.com website")
@allure.description("TC#1 - Simple Login check on vwo.com Website.")
def test_vwologin_positive():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")

    email_input.send_keys("kbddxj8813@instantmessage.online")
    pass_input.send_keys("Wingify@123")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()


    wait = WebDriverWait(driver=driver, timeout=30)
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, "//h4[@data-qa='cotirufajo']"), "Set Up Your Account"))
    # EC.visibility_of(By.CSS_SELECTOR,".page-heading")
    # EC.presence_of_element_located((By.CSS_SELECTOR, ".page-heading"))

    heading_element = driver.find_element(By.XPATH, "//h4[@data-qa='cotirufajo']")
    assert heading_element.text == "Set Up Your Account"
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
