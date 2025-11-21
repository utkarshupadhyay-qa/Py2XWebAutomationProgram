import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_practice():
    driver = webdriver.Chrome()
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")
    driver.maximize_window()
    time.sleep(10)

    search_city = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_city.send_keys("India")

    time.sleep(5)

    list_of_states = driver.find_elements(By.XPATH, "//div[@class='flex flex-col max-sm:gap-[0.5em]']/a/div[1]")
    print("Name" + " | " + "ACQ" + " | " + "Rank")

    for state in list_of_states:
        if "India" in state.text:
            s1 = driver.find_element(locate_with(By.TAG_NAME, "div").to_right_of(state)).text
            s2 = driver.find_element(locate_with(By.TAG_NAME, "p").to_left_of(state)).text
            #s3 = driver.find_element(locate_with(By.TAG_NAME, "div").below(state)).text
            #s4 = driver.find_element(locate_with(By.TAG_NAME, "div").above(state)).text
            print(state.text + " | " + s1 + " | " + s2)
            #print(state.text + " | " + s3 + " | " + s4)



    time.sleep(15)
    driver.quit()