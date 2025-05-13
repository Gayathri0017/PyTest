import time
import pytest
from selenium.webdriver.common.by import By
class TestSearch:
    def test_hp(self,setUp):
        driver=setUp
        driver.find_element(By.NAME, "search").send_keys("Hp")
        driver.find_element(By.CLASS_NAME, "btn-default").click()
        time.sleep(2)
        text = driver.find_element(By.XPATH, "//div[@class='caption']//h4/a").text
        assert "HP" in text
    def test_Honda(self,setUp):
        driver=setUp
        driver.find_element(By.NAME, "search").send_keys("Honda")
        driver.find_element(By.CLASS_NAME, "btn-default").click()
        time.sleep(2)
        text=driver.find_element(By.XPATH, "//*[@id='content']/p[2]").text
        assert "There is no product that matches the search criteria." in text
    def test_Empty(self,setUp):
        driver=setUp
        driver.find_element(By.NAME, "search").send_keys("")
        driver.find_element(By.CLASS_NAME, "btn-default").click()
        time.sleep(2)
        text = driver.find_element(By.XPATH, "//*[@id='content']/p[2]").text
        assert "There is no product that matches the search criteria." in text
