from selenium import webdriver
# 指定浏览器启动地址
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 访问网址
url = 'http://www.jd.com'
browser.get(url)

# page_source获取网页源码数据
context = browser.page_source
print(context)
