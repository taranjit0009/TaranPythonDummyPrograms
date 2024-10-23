import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.service import Service
# from alerthandling import driver

class FunctionalAutomation:

    def __init__(self):
        pass
    #service = Service("D:/driver/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Firefox()
    URL = "https://rahulshettyacademy.com/seleniumPractise/#/"

    def functionalAuto(self):

        wait = WebDriverWait(self.driver,25)
        self.driver.maximize_window()

        self.driver.get(self.URL)

        self.driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("Ber")
        # Wait until the products are loaded
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='products-wrapper']/div/div")))


        results = self.driver.find_elements(By.XPATH,"//div[@class='products']/div")
        len(results)
        assert len(results) > 0
        expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
        actualList = []
        for result in results:
            actualList.append(result.find_element(By.XPATH,"h4").text)
            result.find_element(By.XPATH,"div/button").click()
        print(actualList)
        assert expectedList == actualList
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[class='cart-icon']"))).click()
        #self.driver.find_element(By.CSS_SELECTOR,"a[class='cart-icon']").click()
        #self.driver.find_element(By.XPATH,"//*[text()='PROCEED TO CHECKOUT']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='PROCEED TO CHECKOUT']"))).click()


        #self.driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys('rahulshettyacademy')
        wait.until(EC.presence_of_element_located((By.XPATH,"//input[@class='promoCode']"))).send_keys('rahulshettyacademy')
        self.driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()

        promoMessage = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
        print(promoMessage.text)
        assert promoMessage.text == "Code applied ..!"

        #Sum Validation
        prices = self.driver.find_elements(By.XPATH,"//tr/td[5]/p")
        sum = 0
        for price in prices:
            sum = sum + int(price.text)

        print(sum)
        total = wait.until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/span[1]"))).text
        try:
            assert sum == int(total)
        except Exception as e:
            print(e)
        self.driver.close()


objFun = FunctionalAutomation()

objFun.functionalAuto()
