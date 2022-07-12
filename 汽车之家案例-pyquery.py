# https://car.autohome.com.cn/price/list-15_20-0-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html
# https://car.autohome.com.cn/price/list-15_20-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2.html
# https://car.autohome.com.cn/price/list-15_20-0-0-0-0-0-0-0-0-0-0-0-0-0-0-3.html
import requests
from pyquery import PyQuery

page = 1
url = 'https://car.autohome.com.cn/price/list-15_20-0-0-0-0-0-0-0-0-0-0-0-0-0-0-' + str(page) + '.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                  "Chrome/22.0.1207.1 Safari/537.1"
}

response = requests.get(url=url, headers=headers)
content = response.text

doc = PyQuery(content)

info_list = doc('#brandtab-1 .list-cont').items()

for item in info_list:
    src_url = 'https:' + item('.list-cont-bg .list-cont-img a img').attr('src')
    name = item('.list-cont-bg .list-cont-main .main-title a').text()

    print(src_url + '    ' + name)
