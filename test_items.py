import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 







def test_find_button_add_book (browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    
    

    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), 'Кнопка добавления товара в корзину отсутсвует'
    time.sleep(3)