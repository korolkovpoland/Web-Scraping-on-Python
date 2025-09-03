import requests
from bs4 import BeautifulSoup
import json

for x in range(4,6):
    url = f'https://io.gidonline.fun/home/page-{x}/'

    headers = {
    'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)
    src = response.text
    soup = BeautifulSoup(src, 'lxml')

    with open('Hello_world.html', 'w', encoding='utf-8') as file:
        file.write(src)

    with open('Hello_world.html', encoding='utf-8') as file:
        src = file.read()


    all_product_hrefs = soup.find_all('div', class_='b-content__inline_item short-story')

    items = []

    for item in all_product_hrefs:
        link = item.find('a').get('href')
        name = item.find('div', class_= 'b-content__inline_item-link').find('a').get_text(strip=True)
        genre = item.find('div', class_='misc').get_text(strip=True)
        items.append({'Title': name,'Genre': genre,'url': link})

        print(f'Жанр: {genre}, Название фильма: {name}, ссылка на фильм: {url+link[1:]}')

    with open('file_json.json', 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=4, ensure_ascii=False)
