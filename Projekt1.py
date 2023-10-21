from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions

#import time

driver = webdriver.Chrome()
driver.get('https://www.topestetic.pl/')




search_field = driver.find_element(By.NAME,'q')
search_field.clear()
#driver.find_element(By.NAME,'q').submit()
#time.sleep(5)
search_field.send_keys("Serum")
search_field.send_keys(Keys.RETURN)
#search_button.send_keys('Serum')







driver.quit()

