import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium 4


# @pytest.mark.smoke
def test_vwologin_negative_tc():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    # In HTML Elements this is the order:-
    # id -> name -> className -> tagName -> LinkText, PartialText -> css Selector -> Xpath

    # For "email" HTML elements is as follows:-
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # data-qa="hocewoqisi"
    # >
    # It has 4 attributes
    email_element = driver.find_element(By.NAME , "username")  # By.NAME -> NAME will be uppercase in python
                                                                     # IN JAVA it will be lowercase
    email_element.send_keys("admin")

    time.sleep(10)

    # For "Password" HTML elements is as follows:-

    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # >
    # It has 5 attributes

    password_element = driver.find_element(By.ID , "login-password")
    password_element.send_keys("admin")

    time.sleep(5)

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    time.sleep(5)

    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()