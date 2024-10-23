import time
from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver.ie.service import Service
# driver = nullcontext
#
# def openbrowser():
#     driver.get('https://www.shiksha.com/online-courses/articles/star-pattern-in-python-blogId-144875')
#     driver.maximize_window()
#     print(driver.title)
#     time.sleep(2)
#     driver.close()
#
# browser = str(input('Enter browser option like chrome,firefox,edge = '))
# match browser:
#     case 'chrome':
#         obj_Service = Service("D:/driver/chromedriver-win64/chromedriver.exe")
#
#         driver = webdriver.Chrome(service=obj_Service)
#         openbrowser()
#
#     case 'firefox':
#         driver = webdriver.Firefox()
#         openbrowser()
#
#     case _:
#         driver = webdriver.Edge()
#         openbrowser()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

driver = None  # Initialize driver as None

def open_browser():
    if driver:  # Make sure the driver is initialized
        driver.get('https://www.shiksha.com/online-courses/articles/star-pattern-in-python-blogId-144875')
        driver.maximize_window()
        print(driver.title)
        print(driver.current_url)
        time.sleep(2)
        driver.close()

while True:
    def get_browser_choice():
        return str(input('Enter browser option like chrome, firefox, edge1: ')).strip().lower()


    match get_browser_choice():
        case 'chrome':
            chrome_service = ChromeService("D:/driver/chromedriver-win64/chromedriver.exe")
            driver = webdriver.Chrome(service=chrome_service)
            open_browser()
            break
        case 'firefox':
            firefox_service = FirefoxService()
            driver = webdriver.Firefox(service=firefox_service)
            open_browser()
            break
        case 'edge':
            edge_service = EdgeService()
            driver = webdriver.Edge(service=edge_service)
            open_browser()
            break
        case _:
            print("Invalid browser option. Please enter chrome, firefox, or edge.")
            get_browser_choice()
