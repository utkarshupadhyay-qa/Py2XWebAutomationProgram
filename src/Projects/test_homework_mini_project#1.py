# Selenium Project#1 - Mini Project
# 1- open the url - https://katalon-demo-cura.herokuapp.com/
# 2- click on the make appointment button
# 3-verify that url changes - assert
# 4- time.sleep(3)
# 5- enter the username, password
# 6- next page verify the current url
# 7- make appointment text on the web page.

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# @pytest.mark.smoke
def test_open_katalon_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # HTML Elements of Make Appointment:
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    #
    # class ="btn btn-dark btn-lg"
    # >
    # Make Appointment
    # < / a >

    appointment_element = driver.find_element(By.ID , "btn-make-appointment")
    appointment_element.click()

    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)

    # HTML Elements of Username
    # <
    # input
    # type = "text"
    #
    # class ="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value="" autocomplete="off"
    # >

    username_element = driver.find_element(By.ID , "txt-username")
    username_element.send_keys("John Doe")

    time.sleep(5)

    # HTML elements of password:
    # <
    # input
    # type = "password"
    #
    # class ="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password"
    # value="" autocomplete="off"
    # >

    password_element = driver.find_element(By.ID , "txt-password")
    password_element.send_keys("ThisIsNotAPassword")
    time.sleep(10)

    # HTML elements for Login button :
    # <
    # button
    # id = "btn-login"
    # type = "submit"
    #
    # class ="btn btn-default"
    # >
    # Login
    # <
    # / button
    # >

    login_element = driver.find_element(By.ID , "btn-login")
    login_element.click()
    time.sleep(5)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(5)


    # HTML tag of "Make Appointment" text:
    # <
    # h2
    # >
    # Make
    # Appointment
    # <
    # / h2
    # >

    text_appointment_element = driver.find_element(By.TAG_NAME , "h2").text
    print(text_appointment_element)
    assert text_appointment_element == "Make Appointment"
    driver.quit()