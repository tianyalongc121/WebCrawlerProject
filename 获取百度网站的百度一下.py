import urllib.request
from lxml import etree

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/102.0.0.0 '
                  'Safari/537.36 '
}

# 请求对象的定制
request = urllib.request.Request(url, headers=headers)

# 模拟浏览器访问服务器
response = urllib.request.urlopen(request)

# 获取页面源码
content = response.read().decode('utf-8')

# print(content)

# 解析网页源码 获取所需要的数据

# 解析服务器想要的文件
tree = etree.HTML(content)

# 获取所需要的数据
result = tree.xpath('//input[@id="su"]/@value')[0]

print(result)
