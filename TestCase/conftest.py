import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    chrome_obj = Service("D:/auto/chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_obj)
    driver.maximize_window()
    request.cls.driver = driver
    driver.get("https://magento.softwaretestingboard.com/")
    driver.implicitly_wait(5)
    # driver.find_element(By.CSS_SELECTOR, "").is_displayed()
    yield
    driver.close()
