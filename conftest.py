import pytest
from selenium import webdriver
@pytest.fixture(params=["chrome", "firefox", "edge"])
def setUp(request):
    if request.param=="chrome":
        driver = webdriver.Chrome()
    elif request.param=="firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Edge()

    driver.maximize_window()
    driver.get("https://www.google.com/")
    request.cls.driver = driver
    yield driver
    driver.quit()
