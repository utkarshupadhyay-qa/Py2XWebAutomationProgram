# https://codepen.io/AbdullahSajjad/full/LYGVRgK
# Switch Iframe - result
# Find the button click on it
# Find the input username
# Below element - error message
# Assert that error message.



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_project_iframe_7():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")

    driver.maximize_window()

    time.sleep(5)

    iframe = driver.find_element(By.ID,"result")

    driver.switch_to.frame(iframe)

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    username_element = driver.find_element(By.XPATH, "//input[@id='username']")

    username_error = driver.find_element(locate_with(By.TAG_NAME,"small").below(username_element))
    print(username_error.text)

    assert username_error.text == "Username must be at least 3 characters"

    time.sleep(10)
    driver.quit()

