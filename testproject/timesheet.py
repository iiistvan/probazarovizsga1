# 3 Feladat: Timesheet automatizálása

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html")


# időzítés a tesztesetekhez
def ts():
    time.sleep(2)


# adatbevitel óra és perc
def data_input():
    time_hour_input = driver.find_element_by_xpath('//input[2]')
    time_minute_input = driver.find_element_by_xpath('//input[3]')
    ts()
    time_hour_input.clear()
    ts()
    time_hour_input.send_keys('2')
    ts()
    time_minute_input.clear()
    ts()
    time_minute_input.send_keys('0')


# TC01: üres kitöltés helyessége (kötelező mezők: óra, perc, email)
data_input()
assert not driver.find_element_by_xpath('//*[@id="buttons"]/input[@disabled="disabled"]').is_enabled()

# TC02: helyes kitöltés helyes köszönet képernyő
data_input()
email_input = driver.find_element_by_xpath('//input[1]')
ts()
email_input.send_keys('test@bela.hu')
ts()
driver.find_element_by_tag_name('textarea').send_keys('working hard')
ts()
driver.find_element_by_xpath('//*[@id="dropDown"]/option').click()
ts()
driver.find_element_by_xpath('//*[@id="buttons"]/input').click()
ts()

# eredmény vizsgálata
assert driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[1]').text == '2'
assert driver.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[2]').text == '0'

driver.close()
driver.quit()

