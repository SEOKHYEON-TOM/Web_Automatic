import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 크롬 드라이버 생성
driver = webdriver.Chrome(r"C:\Users\TOM\Desktop\chromedriver_win32\chromedriver.exe")

driver.get('https://workey.codeit.kr/music')
time.sleep(1)

populart_artists = []
#
# for artist in driver.find_elements_by_css_selector('ul.popular__order li'):
#     populart_artists.append(artist.text.strip())
for artist in driver.find_elements(By.CSS_SELECTOR, 'ul.popular__order li'):
    populart_artists.append(artist.text.strip())

print(populart_artists)