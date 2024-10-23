import time

from pycparser.c_ast import Switch
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#from invokingBrowser import driver


class TestAlert:

    def __init__(self,driver):
        self.driver = driver

    def alert(self):
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        self.driver.find_element(By.ID,"name").send_keys("TaranTest Alert")
        self.driver.find_element(By.ID,"alertbtn").click()

        # Wait for the alert to be present instead of using time.sleep()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        #Selecting alert
        alert = self.driver.switch_to.alert

        #printing alert text
        txt = alert.text
        print(txt)
        #Accepting alert
        alert.accept()
    def confirmation(self):
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        self.driver.find_element(By.ID, "name").send_keys("TaranTest Alert")
        self.driver.find_element(By.ID,'confirmbtn').click()

        alert = self.driver.switch_to.alert
        alert.dismiss()
        time.sleep(10)
# Initialize WebDriver
driver = webdriver.Chrome()

objAlert = TestAlert(driver)
objAlert.confirmation()