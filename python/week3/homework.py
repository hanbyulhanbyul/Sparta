import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# 순위 / 곡 제목 / 가수 (네이버영화 실습과 동일하게 진행)

ranking = soup.select('table > tbody > tr > td.number')
# for rank in ranking:
    # print(rank.text.split(' ')[0].strip())

titles = soup.select('a.title.ellipsis')
# for title in titles:
#     print(title.text.strip())

artists = soup.select('a.artist.ellipsis')
# for artist in artists:
    # print(artist.text)
# #

sla = '/'
for i in range(len(titles)):
    print(ranking[i].text.split(' ')[0].strip(),sla , titles[i].text.strip(),sla , artists[i].text)
#



