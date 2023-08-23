import time

import pytest
from urllib3 import request

from PageObject.CreatUsrPageObj import createUser
from PageObject.HomePageObj import Header
from TestData.CreateCustData import userdata
from Utilities.BaseClass import baseclass


class Test_UserCreate(baseclass):
    def test_FieldValidationCheck(self):
        header = Header(self.driver)
        createuser = createUser(self.driver)
        header.CrtUserBtn().click()
        createuser.createbtn().click()
        createuser.assrterr()  # NEED LOG HERE
        time.sleep(3)

    def test_CheckWithDuplicatEmail(self, getUserData):
        header = Header(self.driver)
        createuser = createUser(self.driver)
        header.CrtUserBtn().click()
        createuser.firstname().send_keys(getUserData["firstname"])
        createuser.lastname().send_keys(getUserData["lastname"])
        createuser.emailid().send_keys(getUserData["email"])
        createuser.passwrd().send_keys(getUserData["password"])
        createuser.confirmpass().send_keys(getUserData["password"])
        createuser.createbtn().click()
        self.WaitForEle("//div[@role='alert']")
        createuser.errorheader()
        time.sleep(6)

        print("Case2")
