import time
from selenium import webdriver

# 크롬 드라이버 생성
driver = webdriver.Chrome(r"C:\Users\TOM\Desktop\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1) # 5초 동안 멈췄다가 로그인, 웹페이지의 코드가 로딩되가나 바뀌는 코드 뒤에 넣어주면 좋음
driver.find_element_by_css_selector('.top-nav__login-link').click()
time.sleep(1)
driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
# driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-input').send_keys('codeit')
# copy -> copy selector로 눌렀을 때
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')

driver.find_element_by_css_selector('.login-container__login-button').click()
