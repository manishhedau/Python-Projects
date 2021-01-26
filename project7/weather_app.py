import requests
from bs4 import BeautifulSoup

search = 'weather in sausar'
url = f'https://www.googlr.com/search?q={search}'

res = requests.get(url)
print(res.status_code)

source = BeautifulSoup(res.text,'html.parser')

tempreture = source.find('span',{'id':'wob_tm'}).text
print(tempreture)