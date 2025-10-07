# As we are using Selenium 4 -> so can directly import web driver

from selenium import webdriver

# Selenium 4

def test_open_vwologin():
    driver = webdriver.Chrome() # Starts the Chrome Browser
    driver.get("https://app.vwo.com")   # .get() ->Starts API communication with Chrome Browser driver
                                        # for a GET request to open this URL -> Now Chrome Browser driver
                                        #  will open with this URL in Chrome browser

# Python Interpreter -> optimize if there is no command =>I will stop the execution.
# get -> Navigate the browser to the specified URL in the current window or tab.