# 5 Feladat: Landtransfer tax automatizálása

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html")


# időzítés a tesztesetekhez
def ts():
    time.sleep(2)


# TC01: üres kitöltés helyessége
button = driver.find_element_by_xpath('//button')
button.click()
ts()
assert driver.find_element_by_id('tax').get_attribute('value') == ''
assert driver.find_element_by_id('disclaimer').text == 'Enter the property value before clicking Go button.'

# TC02: helyes kitöltés helyes kitöltése
driver.find_element_by_id('price').send_keys('33333')
ts()
button.click()
ts()
try:
    assert driver.find_element_by_id('tax').get_attribute('value') == '16.665'
except:
    print('A várt érték eltér!')
    print(driver.find_element_by_id('tax').get_attribute('value'))

# ablak lezárása, memória felszabadítása
driver.close()
driver.quit()
