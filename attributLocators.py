import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')
print(driver.title)
print(driver.current_url)
driver.find_element(By.CSS_SELECTOR,"input[class='form-control ng-untouched ng-pristine ng-invalid']").send_keys('ABCD')
driver.find_element(By.NAME,"email").send_keys('hello@gmail.com')
driver.find_element(By.ID,'exampleInputPassword1').send_keys('123456789')
driver.find_element(By.ID,'exampleCheck1').click()

#$x("//input[@value='Submit']") for browser console checking "xpath syntax"

driver.find_element(By.XPATH,"//input[@value='Submit']").click()

textMessage = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

print(textMessage)
assert 'Success' in textMessage

time.sleep(2)