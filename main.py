import requests
from bs4 import BeautifulSoup

# response = requests.get("https://workey.codeit.kr/ratings/index")
# rating_page = response.text
#
# soup = BeautifulSoup(rating_page, 'html.parser') # parser로 html을 정리함
# print(soup.prettify())
# print(soup.select('title')) # 'title'태그를 가져옮
# print(soup.select('td.program'))

# program_title_tags = soup.select('td.program')
# program_titles = []
# for tag in program_title_tags:
#     program_titles.append(tag.get_text())
# print(program_titles)

# print(soup.select_one('td.program')) # td.program인 애들 중 제일 위에 있는 놈 출력
#
# # print(soup.select('td')[:4])
# #
# # td_tags = soup.select('td')[:4]
# #
# # for tag in td_tags:
# #     print(tag.get_text())
#
# print(soup.select('tr')[1])
#
# tr_tag = soup.select('tr')[1]  # 특정 태그 안에서 태그 찾기
# td_tags = tr_tag.select('td')
# # td_tags = tr_tag.select('*') # tr태그 안에 td태그 밖에 없기 때문에
# print(td_tags)
#
# for tag in td_tags:
#     print(tag.get_text())

response = requests.get('https://workey.codeit.kr/music')
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')
print(soup.select('ul.popular__order li')) # ul.popular__order 안에 li만 select

popular_artists = []

# 태그 안에 있는 요소들 하나의 문자열로
# for tag in soup.select('ul.popular__order li'):
#     popular_artists.append(tag.get_text().strip())
#
# print(popular_artists)

# 태그 안에 있는 요소들 리스트의 각 항목으로
for tag in soup.select('ul.popular__order li'):
    # print(tag.strings) # 출력 안됨
    # print(list(tag.strings))
    # print(list(tag.stripped_strings)) # 좀 더 깔끔하게
    # print(list(tag.stripped_strings)[1]) # 원하는 아티스트 이름만
    popular_artists.append(list(tag.stripped_strings)[1])

print(popular_artists)


