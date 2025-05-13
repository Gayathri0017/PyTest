import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=None
def setup_function(function):
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
def teardown_function(function):
    global driver
    driver.quit()
@pytest.mark.smoke
def test_search():
    global driver
    search_box=WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
    )
    search_box.send_keys("Selenium")
    search_box.submit()
    time.sleep(2)
    assert "Selenium" in driver.title
def test_search1():
    global driver
    search_box=WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
    )
    search_box.send_keys("TestNg")
    search_box.submit()
    time.sleep(2)
    assert "TestNg" in driver.title
