import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains




class Actions:
    def __init__(self):
        pass
    URL = 'https://rahulshettyacademy.com/AutomationPractice/'
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    def action(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)

        #Wait class object
        wait  = WebDriverWait(self.driver,20)
        try:
            #Action class object
            action = ActionChains(self.driver)

            hoverElement = self.driver.find_element(By.ID,"mousehover")



            action.click_and_hold(hoverElement).perform()

            rightClick = self.driver.find_element(By.LINK_TEXT, "Top")

            action.context_click(rightClick).perform()

            action.move_to_element(self.driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
            time.sleep(10)
        except Exception as e:
            print(e)

objAction = Actions()
objAction.action()