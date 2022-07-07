import requests
from bs4 import BeautifulSoup

url = 'https://cn.pornhub.com/'

res = requests.get(url)

content = res.text

print(content)

# soup = BeautifulSoup(content, 'xml')
# obj = soup.select('//*[@id="v409365151"]/div/div[3]/span/a/@href')
#
# print(obj)

