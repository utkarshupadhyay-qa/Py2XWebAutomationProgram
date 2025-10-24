import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")

    # Create an Object of Action Chain Class
    actions = ActionChains(driver) # Remember we need to pass driver in the Action Chain Class
    # Send keys but with the Shift
    # Press Shift key down
    # press Shift key up (release)
    actions\
        .key_down(Keys.SHIFT)\
        .send_keys_to_element(first_name,"the testing academy")\
        .key_up(Keys.SHIFT).perform()     # perform() will perform all the stored action
    # the testing academy
    # THE TESTING ACADEMY
    time.sleep(20)

    # url = driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Download File']")
    # actions.context_click(url).perform()

    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions.send_keys("Selenium")

    time.sleep(20)