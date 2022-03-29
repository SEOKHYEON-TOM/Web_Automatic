import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 워크북 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['제품명', '제품이미지주소', '용량', '가격'])

for page in range(1, 8):
    url = f'http://search.danawa.com/dsearch.php?query=%EC%9D%B8%ED%85%9412%EC%84%B8%EB%8C%80%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EC%9D%B8%ED%85%9412%EC%84%B8%EB%8C%80%EB%85%B8%ED%8A%B8%EB%B6%81&previousKeyword=%EC%9D%B8%ED%85%9412%EC%84%B8%EB%8C%80%EB%85%B8%ED%8A%B8%EB%B6%81&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10581%7C0&defaultVmTab=289&defaultVaTab=218&tab=goods'
    response = requests.get(url)
    rating_page = response.text
    soup = BeautifulSoup(rating_page, 'html.parser')

    product_tags = soup.select('div.prod_main_info')

