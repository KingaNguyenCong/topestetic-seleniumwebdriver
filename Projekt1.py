from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

import time

driver = webdriver.Chrome()
driver.get('https://www.topestetic.pl/')
driver.maximize_window()

time.sleep(5)

#Test okna wyszukiwarki

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


#Test dodawania do koszyka

add_to_card = driver.find_elements(By.CLASS_NAME, 'dodaj-koszyk')

time.sleep(5)

add_to_card[1].click()

time.sleep(5)

print("Produkt został dodany do koszyka.")


#do_koszyka_element = WebDriverWait(driver, 10).until(
#    EC.element_to_be_clickable((By.XPATH, '//a[@data-key="0"]'))
#)
#do_koszyka_element.click()

checkout_button = driver.find_element(By.CSS_SELECTOR, '.przejdz-koszyk.przejdz-akcja')
#mogla byc by.class ale jest spacja w nazwie klasy i lepiej css_selector i wtedy te kropki

checkout_button.click()


#Test kupna produktu bez rejestracji

# Przewiń stronę o 1000 pikseli w dół
driver.execute_script("window.scrollBy(0, 1000);")

time.sleep(2)

buy_product_button = driver.find_element(By.CSS_SELECTOR, '.przejdz-koszyk.dodaj-duzy')

buy_product_button.click()

buy_as_guest_button = driver.find_element(By.CSS_SELECTOR, '.zwykly-button.szybkie-zakupy')

buy_as_guest_button.click()

print("Zakupy bez rejestracji.")





driver.quit()

