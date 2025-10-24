import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

def test_03_actions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    iframe = driver.find_element(By.TAG_NAME,"iframe")
    # ActionChains(driver).scroll_to_element(iframe).perform()
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(driver).scroll_from_origin(scroll_origin,0,200).perform()
    # helps us to scroll in iframe 

    # hoverable = driver.find_element(By.ID, "hover")
    # ActionChains(driver)\
    #         .move_to_element(hoverable)\
    #         .perform()
    #

    # draggable = driver.find_element(By.ID, "draggable")
    # droppable = driver.find_element(By.ID, "droppable")
    # ActionChains(driver).drag_and_drop(draggable,droppable).perform()
    # # ActionChains(driver).drag_and_drop_by_offset(draggable,droppable).perform()



    time.sleep(30)