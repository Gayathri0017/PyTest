import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
@pytest.mark.usefixtures("setUp")
class TestGoogleSearch:
    @pytest.mark.parametrize("search_term", ["Selenium WebDriver", "PyTest Tutorial", "Python programming"])
    def test_google_search(self, search_term):
        driver = self.driver
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//textarea[@class='gLFyf']"))
        )
        search_box.send_keys(search_term)
        search_box.submit()
        time.sleep(2)
