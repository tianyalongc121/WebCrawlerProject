from selenium import webdriver
import time

# todo ...有点问题

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

time.sleep(2)

input = browser.find_element_by_id('kw')
input.send_keys('蝙蝠侠')

time.sleep(2)

button = browser.find_element_by_id('su')
button.click()

time.sleep(2)

js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(1)

next_button = browser.find_element_by_xpath('//a[@class="n"]')
next_button.click()

time.sleep(1)

browser.back()

time.sleep(2)

browser.forward()

time.sleep(3)

browser.quit()
