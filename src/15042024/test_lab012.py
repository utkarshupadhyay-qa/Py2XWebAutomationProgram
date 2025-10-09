from selenium import webdriver
import time
import pytest
# Selenium 4
import logging


# @pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(25) # Telling to Python Interpreter.- wait for the 25 seconds, not to the webdriver.
    driver.get("https://google.com") # get command is used to navigate to different URLs
    print(driver.title)