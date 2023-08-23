import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestData.CreateCustData import userdata


@pytest.mark.usefixtures("setup")
class baseclass:

    # For Get Data from Taple
    # @pytest.fixture(params= userdata.Detail)
    # def getUserData(self, request):
    #     return request.param

    @pytest.fixture(params= userdata.exldata())
    def getUserData(self, request):
        return request.param

    def WaitForEle(self, errpath):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located((By.XPATH, errpath)))

    def logDemo(self):
        logger = logging.getLogger(__name__)

        # File Handler
        fileHandle = logging.FileHandler('logfile1.log')
        logger.addHandler(fileHandle)  # FileHandler Object

        # Format of Logger Format is (DateWith time : Level : Testcase name : Message)
        formatofLog = logging.Formatter("%(levelname)s : %(name)s : %(message)s : %(asctime)s")
        fileHandle.setFormatter(formatofLog)  # giving Format information to logger object
        logger.addHandler(fileHandle)
        logger.setLevel(logging.DEBUG)
        return
        # logger.debug("Debug log-------------")
        # logger.info("Info lof*************************-")
        # logger.warning("Warning log /////////////////--------------")
        # logger.error("Error log ''''''''''''''''''''''''''''++++++++")
        # logger.critical("Critical logggg ++++++/-*-*/*-/+*/-*/-")


