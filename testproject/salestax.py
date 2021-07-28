# 2 Feladat: Sales tax applikáció funkcióinak automatizálása

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time
from selenium.webdriver.common.keys import Keys

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html")


def ts():
    time.sleep(2)


# TC01: üres kitöltés helyessége
subtotal_button = driver.find_element_by_id('subtotalBtn')
subtotal_button.click()
ts()
# assert driver.find_element_by_id('subtotal').get_attribute('value') == '0.00'
try:
    assert driver.find_element_by_id('salestax').get_attribute('value') == '0.00'
except:
    print('Nem jelenik meg a 0.00 érték a salestax mezőben!')

calculate_order_button = driver.find_element_by_id('gtotalBtn')
calculate_order_button.click()
ts()
assert driver.find_element_by_id('gtotal').get_attribute('value') == '4.95'

# TC02: 6" x 6" Volkanik Ice kitöltés helyessége
product_item_field = driver.find_element_by_id('Proditem')
product_item_field.click()
ts()
product_item_field.send_keys(Keys.ARROW_DOWN)
ts()
product_item_field.send_keys(Keys.ENTER)
ts()
driver.find_element_by_id('quantity').send_keys('1')
ts()
calculate_order_button.click()
ts()

# várt értékek vizsgálata
try:
    assert driver.find_element_by_id('salestax').get_attribute('value') == '4.95'
except:
    print('Nem jelenik meg a 4.95 érték a salestax mezőben!')
assert driver.find_element_by_id('gtotal').get_attribute('value') == '9.90'

driver.close()
driver.quit()
