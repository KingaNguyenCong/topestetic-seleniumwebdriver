from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.topestetic.pl/')

driver.quit()

