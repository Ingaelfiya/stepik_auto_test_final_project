from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_addtobasketbutton(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button
    
   
