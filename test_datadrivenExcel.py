import time
import pytest
from selenium import webdriver
from utils.excelReader import get_data 
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("uname,p,sts", get_data("D:\\Python_Selenium\\ExcelFiles\\LoginDatas.xlsx", "Sheet1"))
def test_login(uname, p,sts):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.ID, "login2").click()
    time.sleep(3)
    driver.find_element(By.ID, "loginusername").send_keys(uname)
    driver.find_element(By.ID, "loginpassword").send_keys(p)
    driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[3]").click()
    time.sleep(3)
    if sts=="test1":
        txt=driver.find_element(By.ID, "nameofuser").text
        assert uname in txt
    elif sts=="test2":
        txt=driver.switch_to.alert.text
        assert txt=="Wrong password."
    driver.quit()
