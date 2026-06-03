# Login with the Credential - https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# Add user https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser
# Search User



import allure
import openpyxl
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_orangehrm_project6():

    driver = webdriver.Chrome()
    driver.get(" https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    driver.maximize_window()

    driver.implicitly_wait(10)

    username = driver.find_element(By.XPATH, "//input[@name='username']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")

    username.send_keys("Admin")
    password.send_keys("admin123")


    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()


    WebDriverWait(driver=driver, timeout=10).until(
        EC.visibility_of_element_located((By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"))
    )


    # driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    admin_button = driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]")  # Got this Xpath from selectors hub

    admin_button.click()

    WebDriverWait(driver=driver, timeout=10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"))
    )

    # driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"

    add_button = driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    add_button.click()

    WebDriverWait(driver=driver, timeout=10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"))
    )

    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser"


    user_roles = driver.find_elements(By.XPATH, "//div[@class='oxd-select-text-input']")

    user_roles[0].click()

    time.sleep(5)

    driver.find_element(By.XPATH, "//div[@role='listbox']//div[2]").click()

    time.sleep(5)

    # Employee_name
    employee_name = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_name.send_keys("Russel")
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@role='listbox']//div[1]").click()

    time.sleep(5)

    # Status
    status = driver.find_elements(By.XPATH, "//div[@class='oxd-select-text-input']")
    status[1].click()
    driver.find_element(By.XPATH, "//div[@role='listbox']//div[2]").click()

    time.sleep(5)

    # Username
    username = driver.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")
    username[1].send_keys("tester11")

    time.sleep(10)

    # Password
    password = driver.find_elements(By.XPATH, "//input[@type='password']")

    password[0].send_keys("wingify@123")

    time.sleep(5)

    password[1].send_keys("wingify@123")

    time.sleep(5)

    save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_button.click()

    driver.implicitly_wait(10)

    allure.attach(driver.get_screenshot_as_png(), name="User Creation Screenshot", attachment_type=AttachmentType.PNG)



    time.sleep(20)


    # Now search for user which we have created

    actions = ActionChains(driver)

    search_user = driver.find_elements(By.XPATH, "//input[@class='oxd-input oxd-input--active']")

    actions.move_to_element(search_user[1]).click(search_user[1]).send_keys("tester11").perform()

    time.sleep(10)

    search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_button.click()

    time.sleep(10)

    # Verifying user is present or not

    search_result = driver.find_element(By.XPATH, "//div[contains(text(),'tester11')]")
    print(search_result.text)
    assert search_result.text == "tester11"

    time.sleep(10)



    driver.quit()