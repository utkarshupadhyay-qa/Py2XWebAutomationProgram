from webbrowser import Chrome

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    driver.maximize_window()

    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Hacker@4321")
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

    time.sleep(10)

