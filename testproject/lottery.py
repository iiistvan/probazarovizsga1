# 4 Feladat: Lottoszámok automatizálása

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time
from selenium.common.exceptions import NoSuchElementException

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html")


# időzítés a tesztesetekhez
def ts():
    time.sleep(2)


# def test_element_does_not_exist():
#     with self.assertRaises(NoSuchElementException):
#         driver.find_element_by_class_name('balls')


# TC01: lotto huzas elott nem ismertek a szamok
# assert test_element_does_not_exist()

# TC02: lottohuzás működik
generate_button = driver.find_element_by_id('draw-number')
for _ in range(6):
    generate_button.click()
    ts()
balls = driver.find_elements_by_class_name('balls')
assert len(balls) == 6
for b in balls:
    assert int(b.text) in range(1, 60)

# TC03: lottohúzás befejeződött
generate_button.click()
ts()
balls = driver.find_elements_by_class_name('balls')
assert len(balls) == 6
