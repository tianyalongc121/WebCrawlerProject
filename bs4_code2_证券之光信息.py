from bs4 import BeautifulSoup
import urllib.request

url = 'https://quote.stockstar.com/'
context = urllib.request.urlopen(url).read().decode('gb2312')
soup = BeautifulSoup(context, 'lxml')
list = soup.select('#datalist2 .align_left a')
for item in list:
    print(item.get_text())
