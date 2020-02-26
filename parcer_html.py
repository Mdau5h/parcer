import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36'}

base_url = 'https://www.vsemayki.ru/catalog/universities?page=0'
def parce(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    items = []
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': '_3Aqv13MO col-6 col-lg-4 col-xl-3'})
        for div in divs:
            title = div.find('div', attrs={'class': 'ln9is6tg'}).text
            price = div.find('span', attrs={'class': 'price'}).text
            items.append({
                'title': title,
                'price': price
            })
        print(items)

    else:
        print('Error')

parce(base_url, headers)