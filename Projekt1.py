from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

import time

driver = webdriver.Chrome()
driver.get('https://www.topestetic.pl/')

time.sleep(5)
search_button = driver.find_element(By.NAME,'q')
driver.find_element(By.NAME,'q').submit()
#search_button.click()
#search_button.send_keys('Serum')

time.sleep(10)






driver.quit()

