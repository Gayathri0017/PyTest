import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import read_config
bsr=read_config.get_config("Browser","b")
if bsr=="Chrome":
    diver=webdriver.Chrome()
elif bsr=="Edge":
    diver=webdriver.Edge()
diver.maximize_window()
diver.get("https://www.demoblaze.com/")
log=diver.find_element(By.XPATH,value="//a[@id='login2']").click()
time.sleep(3)
un=diver.find_element(By.XPATH,value="//input[@id='loginusername']")
pw=diver.find_element(By.XPATH,value="//input[@id='loginpassword']")
uname=read_config.get_config("data","un")
pwd=read_config.get_config("data","pw")
un.send_keys(uname)
pw.send_keys(pwd)
btn=diver.find_element(By.XPATH,value="(//button[@class='btn btn-primary'])[3]").click()
time.sleep(3)
