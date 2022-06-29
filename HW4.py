import requests
from bs4 import BeautifulSoup

response = requests.get('https://movies.yahoo.com.tw/movie_intheaters.html')

soup = BeautifulSoup(response.text, 'lxml')

info_items = soup.find_all('div', 'release_info')

for item in info_items:
    name = item.find('div', 'release_movie_name').a.text.strip()
    english_name = item.find('div', 'en').a.text.strip()
    release_time = item.find('div', 'release_movie_time').text.strip()
    print(f'{name}({english_name}) 上映日：{release_time} ')