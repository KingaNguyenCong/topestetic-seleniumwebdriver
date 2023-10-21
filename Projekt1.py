from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions

import time

driver = webdriver.Chrome()
driver.get('https://www.topestetic.pl/')
driver.maximize_window()

time.sleep(5)

search_field = driver.find_element(By.NAME,'q')
search_field.clear()
#driver.find_element(By.NAME,'q').submit()
#time.sleep(5)
search_field.send_keys("Serum")
search_field.send_keys(Keys.ENTER)
time.sleep(5)

results = driver.find_elements(By.CSS_SELECTOR, 'div.lista-produkt-content')


if len(results) > 0:
    print("Znaleziono wyniki dla frazy 'Serum'.")
else:
    print("Brak wyników dla frazy 'Serum'.")



driver.quit()

