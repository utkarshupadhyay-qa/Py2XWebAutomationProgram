
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



