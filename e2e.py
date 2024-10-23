import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class E2E:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        #self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait=WebDriverWait(self.driver,20)

    def e2e(self):
        self.driver.get("https://rahulshettyacademy.com/angularpractice")
        self.driver.find_element(By.LINK_TEXT,'Shop').click()

        #Scanning the all products
        products = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")

        for product in products:
            productName = product.find_element(By.XPATH,"div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH,"div/button").click()
                break

        self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()

        self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

        self.driver.find_element(By.ID,"country").send_keys('Ind')

        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))

        self.driver.find_element(By.LINK_TEXT,"India").click()

        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()

        message = self.driver.find_element(By.CLASS_NAME,"alert-success").text

        assert "Success! Thank you" in message
        time.sleep(5)

objE2E = E2E()
objE2E.e2e()