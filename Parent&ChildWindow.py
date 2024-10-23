import time


from selenium import webdriver
from selenium.types import WaitExcTypes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Windows:

    def __init__(self):
        pass

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,20)

    def swith_To_Windows(self):
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/windows")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//div[@id='content']/div/a").click()
        windowsOpen = self.driver.window_handles


        self.driver.switch_to.window(windowsOpen[1])
        txt = self.driver.find_element(By.TAG_NAME,'h3').text
        print(txt)
        self.driver.close()
        self.driver.switch_to.window(windowsOpen[0])

        time.sleep(5)
        parantTxt = self.driver.find_element(By.TAG_NAME,'h3').text
        print(parantTxt)

    def iFramea(self):
        self.driver.get("https://the-internet.herokuapp.com/iframe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//body/div[4]/div[1]/div[1]/button[1]/div[1]/*[1]").click()
        try:
            self.driver.switch_to.frame('mce_0_ifr')

            print(self.driver.find_element(By.XPATH,"//body[@id='tinymce']/p").text)



            self.driver.find_element(By.ID, "tinymce").clear()
            self.driver.find_element(By.XPATH, "//body[@id='tinymce']/p").send_keys("jhsfhasfdkhafdka")
        except Exception as e:
            print(e)
        time.sleep(20)
objWindows = Windows()

#objWindows.swith_To_Windows()

objWindows.iFramea()