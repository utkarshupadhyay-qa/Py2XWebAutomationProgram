import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_01_shadowDOM():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")

    div = driver.find_element(By.XPATH, "//div[@class='jackPart']")

    # Scroll to View to DIV  - for this we need to learn JavaScript Executor

    driver.execute_script("arguments[0].scrollIntoView(true);", div)

    time.sleep(2)

    # Now In div we have to find pizza

    pizza = driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
                                   # return because we want to fetch the element 
    pizza.send_keys("Farmhouse")

    # Handle on Shadow DOM
    # Click on Pizza



    # pizza = driver.find_element(By.ID,"pizza")
    # pizza.send_keys("Farmhouse")
    # Not able to find element - because pizza id is in Shadow Root

    time.sleep(10)
    driver.quit()
