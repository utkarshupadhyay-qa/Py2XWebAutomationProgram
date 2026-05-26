# video - https://www.loom.com/share/fbd5b7436e3b4de48653ddd76b266618
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

# //div[@role='table']/div[2]/div[30]/div[1]/div[4]

# first_part= //div[@role='table']/div[2]/div[
# value changes from 2 to x
# second_part = ]/div[1]/div[
# value changes from 1 to 9
# third_part = ]

# for edit button -   //div[@role='table']/div[2]/div[30]/div[1]/div[4]/following-sibling::div[5]/div/button[2]

# for employee status - //div[@role='table']/div[2]/div[30]/div[1]/div[3]/following-sibling::div[3]
# her 2nd div is changing- div[30] -> div[i]


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_orange_hrm():

    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    driver.maximize_window()

    time.sleep(10)

    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("admin")

    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("Hacker@4321")

    login = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    login.click()


    time.sleep(10)


    # rows

    row_element = driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div")
    rows = len(row_element)
    print(rows)

    # columns
    column_element = driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div[1]/div[1]/div")
    cols = len(column_element)
    print(cols)


    # For employee name - Aman Singhania
    # //div[@role='table']/div[2]/div[30]/div[1]/div[3]
    # first_part = //div[@role='table']/div[2]/div[
    # value changes from 2 to x
    # second part = ]/div[1]/div[
    # value changes from 1 to 9
    # third_part = ]

    first_part = "//div[@role='table']/div[2]/div["
    second_part = "]/div[1]/div["
    third_part = "]"

    for i in range(2, rows+1):
        for j in range(1, cols+1):

            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"

            data = driver.find_element(By.XPATH, dynamic_path).text
            # print(data)

            if "Aman Singhania" in data:
                employee_status_path = f"{dynamic_path}/following-sibling::div[3]"
                employee_status = driver.find_element(By.XPATH, employee_status_path).text
                if "Terminated" in employee_status:
                    delete_button_path = f"{dynamic_path}/following-sibling::div[6]/div/button[1]"
                    driver.find_element(By.XPATH, delete_button_path).click()
                    print("Terminated Employee is deleted")
                    break

