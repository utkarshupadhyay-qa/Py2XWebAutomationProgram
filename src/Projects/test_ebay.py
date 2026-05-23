# Selenium Mini Project #4
#
#
# Open ebay.com.
# Search for the "16 gb"
# Print all the Top 60 Results with there Name and price.
# Give me the cheapest one from the list.



# import time
# import pytest
# import allure
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from allure_commons.types import AttachmentType
#
#
# @pytest.mark.smoke
# @allure.title("Verify ebay test case")
# @allure.description("Verify on ebay.com - on searching 16GB - print 60 results and find the cheapest one")
#
# def test_ebay_mini_project_4():
#     driver = webdriver.Chrome()
#     driver.get("https://www.ebay.com/")
#     driver.maximize_window()
#     time.sleep(10)
#
#     search_element = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
#     search_element.send_keys("16GB")
#
#     search_button = driver.find_element(By.XPATH, "//button[@id='gh-search-btn']")
#     search_button.click()
#
#     time.sleep(10)
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot_LIST", attachment_type= AttachmentType)

#
#     list_of_headings = driver.find_elements(By.XPATH, "//div[@role='heading']")
#
#     for products in list_of_headings:
#         product_names = products.text
#         print(product_names)
#
#     time.sleep(10)
#
#     list_of_price_element = driver.find_elements(By.XPATH,"//span[@class='su-styled-text primary bold large-1 s-card__price']")
#     prize = []
#     for price in list_of_price_element:
#         product_price = price.text
#         print(product_price)
#         x = product_price.replace("$", " ").strip()
#         prize.append(x)
#
#     prize.sort()
#
#     # Minimum price - prize[1]
#
#     print(f"Minimum price is :{prize[1]}" )

#     time.sleep(10)
#
#     driver.quit()






import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType






class Test_loginpage():
    @allure.title("Loginpage")
    @allure.description("#TC1- Verify URL and get list of product after searching keyword")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Nilesh Nikume")
    @allure.link("https://www.ebay.com/", name="Website")
    @allure.testcase("TC-1")
    @pytest.mark.smoke
    def test_open_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ebay.com/")
        driver.maximize_window()


        assert driver.current_url == "https://www.ebay.com/"
        allure.attach(driver.get_screenshot_as_png(), name='Home_Page_Screenshot', attachment_type=AttachmentType.PNG)

        driver.find_element(By.ID, 'gh-ac').send_keys("16gb")
        driver.find_element(By.XPATH, "//button[@id='gh-search-btn']").click()
        allure.attach(driver.get_screenshot_as_png(), name='Product_Page_Screenshot', attachment_type=AttachmentType.PNG)

        list_element = driver.find_elements(By.XPATH, "//span[@role='heading']")
        for item in list_element:
            product_name = item.text
            print(product_name)


        prize_of_elements = driver.find_elements(By.XPATH, "//span[@class ='s-item__price']")
        prize = []
        for item in prize_of_elements:
            text = item.text
            #    print(text)
            #    Remove "$" and any leading/trailing spaces
            x = text.replace("$", "").strip()
            #Handle price ranges like 5.99 to 10.99
            x = x.split(" to ")[0]

            try:
                prize.append(float(x))

            except:
                pass


        print(prize)
        prize.sort()
        lowest_price = min(prize)

        print(f"Lowest price is : {lowest_price}")



        driver.quit()