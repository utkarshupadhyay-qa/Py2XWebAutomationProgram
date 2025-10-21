# WEB TABLES

from pycparser.ply.ctokens import t_DIVIDE
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()


    # First we need to find how many rows and columns it has

    # Row:
    # // table[contains( @ id, 'cust')]/tbody/tr
    row_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)

    # Columns:
    # //table[contains(@id,'cust')]/tbody/tr[2]/td
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    # Will give columns(values) of 2nd row
    col = len(col_elements) # length of columns in 2nd row
    print(col)

# First Part - //table[contains(@id,"cust")]/tbody/tr[
    # 7 - i ( 2,7)   -> This part changes (row number 2 to 7) - so FOR loop (dynamic in nature)
    # Second Part - ]/td[
    # 3 - j ( 1,3)    -> This part changes ( column number 1 to 3) - so FOR loop (dynamic in nature)
    # Third Part - ]

    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2 , row +1):   # range(1,10) -> 1, 9+1)
        for j in range(1 , col +1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"  # We are doing this = to generate all the path
                                                                            # of all the elements
            data = driver.find_element(By.XPATH,dynamic_path).text
            # print(data)
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"   # at end td - because td- tag for columns
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennett is in {country_text}")

            # In interview - they ask -find Helen Bennett and which country she belongs to

    # Dynamic table
    driver.get("https://awesomeqa.com/webtable1.html")
    # Get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")  #tbody because we want only body
    row_table = table.find_elements(By.TAG_NAME, "tr")   # "//table[@summary='Sample Table']/tbody/tr"
    # this is called as Find Element Chaining

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            # print(e.text)
            if "UAE" in e.text:
                print("YES")


# Another example:

# //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    # first part - //div[@role='table']/div[2]/div[
    # 1-9
    # second part - ]/div[1]/div[
    # 1- 9
    # third part ]


 #
    # for i in range(1,10)
    # //div[@role='table']/div[2]/div[i]/div[1]/div[3]/following-sibling::div[3]

