import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import Select


class Page:
    textfield_xpath = "//a[contains(text(),'Text Fields')]"
    textfield_firstname_without_placeholder = "firstName"
    textfield_last_name_with_placeholder = "//input[@id='lastNameWithPlaceholder']"
    radiobutton_id = "sidebaRadioButtons"
    single_select_radio_button_id = "firstSelect1"
    checkbox_id = "sidebarCheckbox"
    single_select_checkbox_id = "firstSelect1"
    def __init__(self, driver):
        self.driver = driver

    def click_textfield(self):
        self.driver.find_element(By.XPATH, self.textfield_xpath).click()

    def enter_first_name(self, value):
        link = self.driver.find_element(By.ID, self.textfield_firstname_without_placeholder)
        link.send_keys(value)

    def enter_last_name(self, value):
        self.driver.find_element(By.XPATH, self.textfield_last_name_with_placeholder).send_keys(value)

    def click_radiobutton(self):
        self.driver.find_element(By.ID, self.radiobutton_id).click()

    def single_select_radio_button_click(self):
        self.driver.find_element(By.ID, self.single_select_radio_button_id).click()

    def click_checkbox(self):
        self.driver.find_element(By.ID, self.checkbox_id).click()

    def single_select_checkbox_click(self):
        self.driver.find_element(By.ID, self.single_select_checkbox_id).click()