from selenium.webdriver.common.by import By


class Header:

    def __init__(self, driver):
        self.driver = driver

    createuser_btn = (By.XPATH, "//div[@class= 'panel header']/ul/li/a[contains(text(),'Create an Account')]")
    sign_in = (By.XPATH, "//div[@class= 'panel header']/ul/li/a[contains(text(),'Sign In')]")
    search_box = (By.CSS_SELECTOR, "#search_autocomplete")
    cart_btn = (By.XPATH, "//a[@class='action showcart']")

    def CrtUserBtn(self):
        return self.driver.find_element(*Header.createuser_btn)

    def SignIn(self):
        return self.driver.find_element(*Header.sign_in)
