import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium 4


# @pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")


    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg"
    # >
    # Make Appointment
    # </a>
# We got the above html code by right click on Make Appointment Button - Inspect - hover over button
# Copy the html element in Element columns while inspecting


    # Find the element with the anchor tag - button
    # Click on it

    # Ways to find element in HTML:-
    # #1 - id, className, name, tagName, linkText and PartialLinkText.
    # #2 - css Selector, xpath(sure shot way to find the elements in the HTML)

# To find 'id' attribute is unique - in inspect CTRL+F and search "btn-make-appointment" it will show 1 of 1
    element = driver.find_element(By.ID , "btn-make-appointment")
    element.click()

    time.sleep(15)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.quit()