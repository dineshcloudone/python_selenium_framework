import os

from pageobjects.HomePage import HomePage
from pageobjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomeString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pdb


class Test_001_AccountReg:

    baseURL = ReadConfig.getApplicationURL() # get value from .ini file
    #baseURL = "https://demo.opencart.com/"
    logger=LogGen.loggen()

    def test_account_reg(self,setup):

        self.logger.info("**** test_001_AccountRegistration started ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("**** Launching application ****")
        self.driver.maximize_window()


        self.hp=HomePage(self.driver)
        #breakpoint()
        self.logger.info("**** clicking on MyAccount registration ****")
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage=AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email=randomeString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        #self.regpage.setEmail("abc1@gmail.com")
        #self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        #self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()
        if self.confmsg=="Your Account Has Been Created!":
            self.logger.info("Account registration is passed...")
            assert True
            self.driver.close()

        else:
            #path = os.path.abspath(os.curdir)
            #print(f"File path is :{path}")
            #print(path+"\\screenshots\\" + "test_account_reg.png")
            #scr=self.driver.get_screenshot_as_file(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_account_reg.png")

            #scr=self.driver.save_screenshot(r"C:\Python\Test_Project\screenshots\test_account_reg.png")
            scr = self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_account_reg.png")
            self.logger.error("Account registration is failed...")
            if scr:
                print("Screenshot taken")
            else:
                print("No Screenshot taken")
            #self.driver.save_screenshot("C:\Python\Test_Project\screenshots\test_account_reg.png")
            self.driver.close()
            assert False
        self.logger.info("**** test_001_AccountRegistration completed ****")
