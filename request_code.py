import requests
#
# url = 'http://baidu.com'
# response = requests.get(url)
# print(response)
#
# ####
#
# data = {
#     'name': '编程帮',
#     'url': "www.biancheng.net"
# }
#
# response = requests.get('http://httpbin.org/get', params=data)
# # 直接拼接参数也可以
# # response = requests.get(http://httpbin.org/get?name=gemey&age=22)
# # 调用响应对象text属性，获取文本信息
# print(response.text)

url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0'
}
# 网上找的免费代理ip
proxies = {
    'https': 'https://202.55.5.209:8090'
}
html = requests.get(url, proxies=proxies, headers=headers, timeout=5).text
print(html)
