# eg:百度翻译

# todo ...有问题

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'
headers = {
    'user‐agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 74.0.3729.169 Safari / 537.36'
}
keyword = input('请输入您要查询的单词: ')
data = {
    'kw': keyword
}
data = urllib.parse.urlencode(data).encode('utf‐8')
request = urllib.request.Request(url=url, headers=headers, data=data)
response = urllib.request.urlopen(request)
print(response.read().decode('utf‐8'))
