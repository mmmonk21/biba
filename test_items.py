from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest
from selenium.webdriver.chrome.options import Options




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    time.sleep(30)
    
    button1 = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")

    assert button1.is_displayed()