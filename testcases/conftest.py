import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Firefox(GeckoDriverManager().install())
    # return driver
    #service = Service(executable_path='C:\\Python\\geckodriver.exe')
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=service, options=options)

    # options = webdriver.FirefoxOptions()
    # driver = webdriver.Firefox(service=service, options=options)

    driver = webdriver.Firefox(executable_path='C:\Python\geckodriver.exe')
    return driver