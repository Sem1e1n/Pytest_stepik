import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 







def test_find_button_add_book (browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    button.click()
    message = browser.find_element(By.CSS_SELECTOR, ".in:nth-child(1) strong")
    print (message)
    assert "Coders at Work" in message.text
    time.sleep(3)