import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.parametrize('b', ["Chrome","Edge"])
@pytest.mark.parametrize('url', ["https://www.amazon.in/","https://www.flipkart.com/"])
def test_Google(b,url):
    if b.__eq__("Chrome"):
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Edge()
    driver.maximize_window()
    driver.get(url)
    print(driver.title)
