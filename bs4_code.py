import urllib.request

from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'

resp = urllib.request.urlopen(url)
context = resp.read().decode('utf-8')
soup = BeautifulSoup(context, 'lxml')
obj = soup.select("ul[class='grid padded-3 product'] div[class='preview circle']")
for item in obj:
    completePicUrl = 'https://www.starbucks.com.cn' + item.attrs.get('style').split('url("')[1].split('")')[0]
    print(completePicUrl)
