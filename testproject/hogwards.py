# 1 Feladat: Hogwards express jegyautomata

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
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html")


def ts():
    time.sleep(1)


testdata_name = 'Molnár István'
testdata_datetime = datetime(2021, 7, 29, 8, 0)

# beviteli mező definiciók
passenger_input_field = driver.find_element_by_id('passenger')
departure_date_input_field = driver.find_element_by_id('departure-date')
departure_time_input_field = driver.find_element_by_id('departure-time')
issue_ticket_button = driver.find_element_by_id('issue-ticket')

# feltöltés teszadatokkal
passenger_input_field.click()
ts()
passenger_input_field.send_keys(testdata_name)
ts()
passenger_input_field.send_keys(Keys.TAB)
ts()
departure_date_input_field.send_keys(testdata_datetime.strftime('%Y\t%m%d'))
ts()
departure_date_input_field.send_keys(Keys.TAB)
ts()
departure_time_input_field.send_keys(testdata_datetime.strftime('%H%M'))
ts()
issue_ticket_button.click()
ts()

# bevitt adatok ellenőrzése
assert driver.find_element_by_id('passenger-name').text == testdata_name.upper()
assert driver.find_element_by_id('departure-date-text').text == testdata_datetime.strftime('%Y-%m-%d')
assert driver.find_element_by_id('side-detparture-date').text == testdata_datetime.strftime('%Y-%m-%d')
assert driver.find_element_by_id('departure-time-text').text == testdata_datetime.strftime('%H:%M%p')
assert driver.find_element_by_id('side-departure-time').text == testdata_datetime.strftime('%H:%M%p')
