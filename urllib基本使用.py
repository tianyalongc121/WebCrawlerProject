import urllib.request

from lxml import etree

url = 'https://www.baidu.com/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

print(content)

tree = etree.parse(content)

# 查找ul下的li
tree.xpath('')

