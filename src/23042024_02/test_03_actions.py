import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

def test_03_actions():
    driver = webdriver.Chrome()

    # For click on click text
    # driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # driver.maximize_window()
    #
    # clickable_text = driver.find_element(By.ID, "clickable")
    # actions = ActionChains(driver)
    # actions.double_click(clickable_text).perform()
    #
    # time.sleep(15)


    # For Hover
    # driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # driver.maximize_window()
    #
    # hover_element = driver.find_element(By.ID,"hover")
    # actions = ActionChains(driver)
    # actions.move_to_element(hover_element).perform()
    # time.sleep(10)



    # For Drag nand Drop
    # driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # driver.maximize_window()
    #
    # draggable_element = driver.find_element(By.ID, "draggable")
    # droppable_element = driver.find_element(By.ID, "droppable")
    # actions = ActionChains(driver)
    # actions.drag_and_drop(draggable_element,droppable_element).perform()
    # time.sleep(10)



    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.TAG_NAME,"iframe")
    # ActionChains(driver).scroll_to_element(iframe).perform()

    # Scroll from an element(iframe) with offset 0,200
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(driver).scroll_from_origin(scroll_origin,0,200).perform()
    # helps us to scroll in iframe


    time.sleep(30)