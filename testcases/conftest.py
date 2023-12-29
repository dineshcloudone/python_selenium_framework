
import pdb

from datetime import datetime
import os

import pytest
from selenium import webdriver

#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    driver=None

    #pdb.set_trace()
    if browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launching firefox browser.........")
    else:
        print("Please give either edge or firefox browser names")
        #driver = webdriver.Chrome7(ChromeDriverManager().install())
        #print("Launching chrome browser.........")
    return driver

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser",action='store',default='chrome')


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    browser_value=request.config.getoption("--browser")
    print(f"Browser value from command line: {browser_value}")
    return browser_value


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"