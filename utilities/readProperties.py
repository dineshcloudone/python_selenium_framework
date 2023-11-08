import configparser
import os

#config = configparser.RawConfigParser()
config = configparser.ConfigParser()
config.read(r'C:\Python\Test_Project\configurations\config.ini')
#config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        print("before getting url")
        url=(config.get('CommonInfo', 'baseURL'))
        print("after getting url")
        return url

    @staticmethod
    def getUseremail():
        username=(config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        password=(config.get('CommonInfo', 'password'))
        return password


#Testing above methods - optional Code
#print(ReadConfig.getApplicationURL())
#print(ReadConfig.getUseremail())