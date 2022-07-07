from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable‐gpu')
# 设置为自己chrome浏览器.exe的系统路径
path = r'C:\Users\99593\AppData\Local\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.baidu.com')
# browser.save_screenshot('baidu.jpg')
