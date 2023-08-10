import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig
#from pageObjects.LoginPage import LoginPage
import time
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def data(setup, request):
    baseURL = ReadConfig.getApplicationURL()
    driver = setup
    driver.get(baseURL)
    time.sleep(5)
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()

@pytest.fixture(scope="class")
def setup(browser):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    print("Launching Chrome browser....")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


# ############## PyTest HTML Report ###############
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'HYPD STORE'
#     config._metadata['Module Name'] = 'Home page'
#     config._metadata['Tester'] = 'Admin'
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("plugins", None)
