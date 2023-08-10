import time

import pytest
from selenium.webdriver.common.keys import Keys
from pageObjects.PG import Page
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("data")
class Test_page:
    logger = LogGen.loggen()
    #baseURL = ReadConfig.getApplicationURL()

    def test_page_001(self):
        self.logger.info("*********** Starting test case PG-001 **********")
        self.pg = Page(self.driver)
        self.driver.implicitly_wait(2)
        self.pg.click_textfield()
        self.driver.implicitly_wait(2)
        self.pg.enter_first_name("chandni")
        time.sleep(2)
        self.pg.enter_last_name("chanana")
        self.driver.implicitly_wait(2)
        self.pg.click_radiobutton()
        self.driver.implicitly_wait(2)
        self.pg.single_select_radio_button_click()
        self.driver.implicitly_wait(2)
        self.pg.click_checkbox()
        time.sleep(2)
        self.pg.single_select_checkbox_click()
        # self.logger.info("*********** landing page URL and title validation started ************")
        # act_URL = self.driver.current_url
        # print(act_URL)
        # act_title = self.driver.title
        # print(act_title)
        # if (act_title == expected_title) and (act_URL == expected_URL):
        #     assert True
        #     time.sleep(2)
        #     self.logger.info("********************* Landing Page URL & title test is passed *********************")
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_LandingPageTitle_and_url.png")
        #     time.sleep(2)
        #     #self.driver.close()
        #     self.logger.error("********************* Landing page URL & title test is failed *********************")
        #     assert False