import requests

nike_pages = []

#2022.03.23 기준 총 39개 목록이 뜸
for i in range(39):
    url = f'https://www.musinsa.com/search/musinsa/goods?q=nike&list_kind=small&sortCode=pop&sub_sort=&page={i}&display_cnt=0&saleGoods=false&includeSoldOut=false&setupGoods=false&popular=false&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=false&d_cat_cd=&attribute='
    response = requests.get(url)
    nike_page = response.text #url로 들어간 홈페이지의 html정보를 nike_page에 저장
    nike_pages.append(nike_page)

print(len(nike_pages))
print(nike_pages[0])
