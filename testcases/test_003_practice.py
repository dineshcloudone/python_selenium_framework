from pageobjects.HomePage import HomePage
from pageobjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pdb
import os

class Test_Practice:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_sel_practice(self,setup):

        print('Inside selenium practice')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        print(self.driver.title)
        self.driver.close()