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

def test_cdnio_miniproject3():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")

    driver.maximize_window()

    