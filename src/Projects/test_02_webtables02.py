# Orange HRM

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)

    # ✅ Wait for username field
    username = wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username.send_keys("admin")

    # ✅ Wait for password field
    password = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password.send_keys("Hacker@4321")

    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    time.sleep(10)

    # //div[@role='table']/div[2]/div[1]/div[1]/div[3]

    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    # fp - //div[@role='table']/div[2]/div[
    # 1-50
    # sp - ]/div[1]/div[
    # 1- 9
    # tp ]

    print("Employee - ", find_employee_status(driver, "Aman"))


def find_rows_col(driver):
    # //div[@role='table']/div[2]/div[1]/div[1]/div[3]

    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    # fp - //div[@role='table']/div[2]/div[
    # 1-9
    # sp - ]/div[1]/div[
    # 1- 9
    # tp ]

    # Row
    # //table[contains(@id,"cust")]/tbody/tr
    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    row_elements = driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div")
    row = len(row_elements)
    print(row)

    # Col
    # // table[contains( @ id, "cust")] / tbody / tr[2] / td
    col_elements = driver.find_elements(By.XPATH, "//div[@role='table']/div[2]/div[1]/div/div")
    col = len(col_elements)
    print(col)
    return row, col


def find_employee_status(driver, employee_name):
    row, col = find_rows_col(driver)

    first_part = "//div[@role='table']/div[2]/div["
    second_part = "]/div/div["
    third_part = "]"
    employee_status = None
    for i in range(1, row + 1):  # range(1,51) -> 1, 50+1
        for j in range(1, col + 1):   # range(
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if employee_name in data:
                employee_status_path = f"{dynamic_path}/following-sibling::div[3]"
                employee_status = driver.find_element(By.XPATH, employee_status_path).text
                print(f"{employee_name} employee status is  {employee_status}")
                if employee_status == "Terminated":
                    edit_employee_status_path = f"{dynamic_path}//following-sibling::div/div/button[1]"
                    driver.find_element(By.XPATH, edit_employee_status_path).click()
                break

    return employee_status

    driver.quit()