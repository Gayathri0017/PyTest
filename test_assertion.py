import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
def test_reg():
    driver=webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    wait=WebDriverWait(driver,10)
    fp=driver.find_element(By.XPATH,value="//div[@id='loginPanel']/p[1]/a")
    reg=driver.find_element(locate_with(By.XPATH,"//div[@id='loginPanel']/p[1]/a/following::a[1]").below(fp))
    reg.click()
    fname=driver.find_element(By.XPATH,value="//input[@id='customer.firstName']")
    fname.send_keys("Gayathri")
    lname=driver.find_element(locate_with(By.XPATH,"//input[@id='customer.firstName']//following::input[1]").below(fname))
    lname.send_keys("R")
    add=driver.find_element(locate_with(By.XPATH,"//input[@id='customer.firstName']//following::input[2]").near(lname))
    add.send_keys("abc")
    city=driver.find_element(By.XPATH,value="//input[@id='customer.address.city']")
    city.send_keys("Salem")
    zip=driver.find_element(By.XPATH,value="//input[@id='customer.address.zipCode']")
    zip.send_keys("630905")
    st=driver.find_element(locate_with(By.XPATH,"//input[@id='customer.address.city']/following::input[1]").above(zip))
    st.send_keys("TamilNadu")
    ph=driver.find_element(locate_with(By.XPATH,"//input[@id='customer.address.zipCode']/following::input[1]").below(zip))
    ph.send_keys("9087564312")
    ssn=driver.find_element(locate_with(By.XPATH,"//input[@id='customer.ssn']").near(ph))
    ssn.send_keys("1234")
    un=driver.find_element(By.XPATH,value="//input[@id='customer.username']")
    un.send_keys("Gayu00900")
    pw=driver.find_element(locate_with(By.XPATH,"//input[@id='customer.username']//following::input[1]").below(un))
    pw.send_keys("Gayu@123")
    cp=driver.find_element(locate_with(By.XPATH,"//input[@id='customer.username']//following::input[2]").near(pw))
    cp.send_keys("Gayu@123")
    btn=driver.find_element(By.XPATH,"//input[@id='customer.username']//following::input[3]")
    btn.click()
    time.sleep(5)
    text=driver.find_element(By.XPATH,value="//h1").text
    # if(text.contains("un")):
    #     print("Pass")
    # else:
    #     print("Fail")

    assert "Gayu0021" in text
    print("After")
# def test_login():
#     uname=driver.find_element(By.XPATH,"//input[@name='username']")
#     uname.send_keys("Gayu0017")
#     pword=driver.find_element(locate_with(By.XPATH,"//input[@name='username']/following::input[1]").near(uname))
#     pword.send_keys("Gayu@123")

#     login=driver.find_element(locate_with(By.XPATH,"//input[@name='username']/following::input[2]").below(pword))
#     wait.until(expected_conditions.element_to_be_clickable(login))
#     login.click()
#     time.sleep(5)