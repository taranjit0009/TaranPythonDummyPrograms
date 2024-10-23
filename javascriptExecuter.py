import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class JavaScriptExecuter:

    def __init__(self):
        # Initialize Chrome options and WebDriver in the constructor
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = ActionChains(self.driver)
    #----------------------------------#
    '''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver,20)
    actions = ActionChains(driver)
    '''
    # ----------------------------------#
    def javaScript_Executer(self):

        self.driver.maximize_window()

        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.execute_script("window.scrollBy(0,700)")
        self.driver.get_screenshot_as_file("Taran.png")

        time.sleep(5)

objJava = JavaScriptExecuter()

objJava.javaScript_Executer()

