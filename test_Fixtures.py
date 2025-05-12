import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture()
def test_setUp():
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()
def test_hp(test_setUp):
    ele=driver.find_element(By.XPATH,value="//input[@name='search']")
    ele.send_keys("Hp")
    btn=driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']")
    btn.click()   
    time.sleep(3)
    txt=driver.find_element(By.XPATH,value="//div[@class='caption']//h4/a").text
    assert(txt.__contains__("HP"))

def test_Honda(test_setUp):
    ele=driver.find_element(By.XPATH,value="//input[@name='search']")
    ele.send_keys("Honda")
    btn=driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']")
    btn.click()   
    time.sleep(3)
    txt=driver.find_element(By.XPATH,value="//*[@id='content']/p[2]").text
    assert(txt.__contains__("There is no product that matches the search criteria."))

def test_Empty(test_setUp):
    ele=driver.find_element(By.XPATH,value="//input[@name='search']")
    ele.send_keys("")
    btn=driver.find_element(By.XPATH,value="//button[@class='btn btn-default btn-lg']")
    btn.click()   
    time.sleep(3)
    txt=driver.find_element(By.XPATH,value="//*[@id='content']/p[2]").text
    assert(txt.__contains__("There is no product that matches the search criteria."))