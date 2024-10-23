import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from invokingBrowser import driver


class StaticDropDown:
    driver = webdriver.Chrome()
    def static_dropdown(self):

        self.driver.get('https://rahulshettyacademy.com/angularpractice/')
        StaticDropDown.driver.maximize_window()

        #Select static DropDown value
        dropdown= Select(StaticDropDown.driver.find_element(By.ID,'exampleFormControlSelect1'))
        dropdown.select_by_visible_text('Female')



    def dynamic_dropdown(self):
        StaticDropDown.driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
        StaticDropDown.driver.find_element(By.ID,'autosuggest').send_keys('ind')
        time.sleep(10)
        countries = StaticDropDown.driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

        for country in countries:
            if country.text == 'India':
                country.click()
                break

        time.sleep(12)
        assert StaticDropDown.driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'

    def explicitWait(self):
        StaticDropDown.driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
        #define wait object
        wait = WebDriverWait(StaticDropDown.driver,10)

        #wait for element to display
        dropdown = wait.until(EC.element_to_be_clickable((By.ID,'autosuggest')))

        dropdown.send_keys("Ind")

        #wait for drop down element visibility
        options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"li[class='ui-menu-item'] a")))

        #Itrate the values and perfrom click action

        for option in options:
            if option.text == 'India':
                option.click()
                break
    def checkButton(self):
        StaticDropDown.driver.maximize_window()
        StaticDropDown.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        options = StaticDropDown.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        for option in options:
            if option.get_attribute('value')=="option2":
                option.click()
                assert option.is_selected()
                break

        time.sleep(20)
    def radioButton(self0):
        StaticDropDown.driver.maximize_window()
        StaticDropDown.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        radioButton = StaticDropDown.driver.find_elements(By.XPATH,"//input[@class='radioButton']")
        radioButton[2].click()
        assert radioButton[2].is_selected()
        time.sleep(10)


objStaticDropDown = StaticDropDown()
objStaticDropDown.checkButton()
objStaticDropDown.radioButton()
#objStaticDropDown.static_dropdown()
#objStaticDropDown.dynamic_dropdown()
#objStaticDropDown.explicitWait()