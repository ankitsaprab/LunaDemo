from selenium.webdriver.common.by import By

from TestData.CreateCustData import userdata


class createUser:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.CSS_SELECTOR, "#firstname")
    first_name_err = (By.CSS_SELECTOR, "#firstname-error")
    last_name = (By.CSS_SELECTOR, "#lastname")
    last_name_err = (By.CSS_SELECTOR, "#lastname-error")
    news_latter = (By.CSS_SELECTOR, "#is_subscribed")
    email = (By.CSS_SELECTOR, "#email_address")
    email_err = (By.CSS_SELECTOR, "#email_address-error")
    password = (By.CSS_SELECTOR, "#password")
    password_err = (By.CSS_SELECTOR, "#password-error")
    confirm_pass = (By.CSS_SELECTOR, "#password-confirmation")
    confirm_pass_err = (By.CSS_SELECTOR, "#password-confirmation-error")
    create_btn = (By.XPATH, "//div[@class='primary']/button/span[contains(text(),'Create an Account')]")
    err_class = (By.XPATH, "//div[@class='control']/div[@class='mage-error']")
    # error_header = (By.XPATH, "//div[@role='alert']/div[@class='message-error error message']/div")

    def assrterr(self):
        error = self.driver.find_elements(*createUser.err_class)
        for err in error:
            assert err.text == "This is a required field.", err.get_attribute("for") + ":" + "Validation Missing or not as Expected."
            print(err.text)
        return

    def firstname(self):
        return self.driver.find_element(*createUser.first_name)

    def firstnameErr(self):
        return self.driver.find_element(*createUser.first_name_err)

    def lastname(self):
        return self.driver.find_element(*createUser.last_name)

    def lastnameErr(self):
        return self.driver.find_element(*createUser.last_name_err)

    def newslatter(self):
        self.driver.find_element(*createUser.news_latter).is_selected()
        return

    def emailid(self):
        return self.driver.find_element(*createUser.email)

    def emailerr(self):
        return self.driver.find_element(*createUser.email_err)

    def passwrd(self):
        return self.driver.find_element(*createUser.password)

    def passwrderr(self):
        return self.driver.find_element(*createUser.password_err)

    def confirmpass(self):
        return self.driver.find_element(*createUser.confirm_pass)

    def confirmpasserr(self):
        return self.driver.find_element(*createUser.confirm_pass_err)

    def createbtn(self):
        return self.driver.find_element(*createUser.create_btn)

    def errorheader(self):
        text = "There is already an account with this email address."
        error_header = self.driver.find_element(By.XPATH, "//div[@role='alert']/div[@class='message-error error message']/div")

        if error_header.is_displayed() and text in error_header.text:
            print("Duplicate Email")
        return
