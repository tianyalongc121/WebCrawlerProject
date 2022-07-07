# import requests
#
# from lxml import etree
#
# url = 'https://bang.dangdang.com/books/fivestars/1-1'
#
# # http://bang.dangdang.com/books/fivestars/1-1
# # http://bang.dangdang.com/books/fivestars/1-2
# # http://bang.dangdang.com/books/fivestars/1-3
#
#
# # /html/body/div[3]/div[3]/div[2]/ul/li[1]/div[3]/a/@title
# # /html/body/div[3]/div[3]/div[2]/ul/li[1]/div[3]/a/@href
#
# # /html/body/div[3]/div[3]/div[2]/ul/li[1]/div[2]/a/img/@src
# # /html/body/div[3]/div[3]/div[2]/ul/li[1]/div[2]/a/img/@title
#
# # /html/body/div[3]/div[3]/div[2]/ul/li[1]/div[1]
#
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;'
#               'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
#     'Connection': 'keep-alive',
#     'Cookie': 'ddscreen=2; ddscreen=2; ddscreen=2; dest_area=country_'
#               'id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_'
#               'id%3D0%26town_id%3D0; __permanent_id=20220706235415844102145815707813075;'
#               ' __visit_id=20220706235415887109653570748922440;'
#               ' __out_refer=1657122856%7C!%7Cwww.google.com%7C!%7C;'
#               ' __rpm=...1657123012088%7C...1657123043047;'
#               ' __trace_id=20220706235723200162161847066171475',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/103.0.0.0 Safari/537.36'
# }
#
# response = requests.get(url=url, headers=headers)
# content = response.text
# # print(content)
#
# etree = etree.HTML(content)
#
# # print(etree)
#
#
#
#
import json
import re

import requests

from bs4 import BeautifulSoup

from lxml import etree


def parse_result(html):
    # pattern = re.compile(
    #     '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
    #     re.S)
    # items = re.findall(pattern, html)
    # for item in items:
    #     yield {
    #         'range': item[0],
    #         'iamge': item[1],
    #         'title': item[2],
    #         'recommend': item[3],
    #         'author': item[4],
    #         'times': item[5],
    #         'price': item[6]
    #     }
    #     print(item)

    soup = BeautifulSoup(html, 'lxml')

    # //div[@class="bang_list_box"]/ul[@class="bang_list clearfix bang_list_mode"]/li/div[@class="name"]
    # //div[@class="bang_list_box"]/ul[@class="bang_list clearfix bang_list_mode"]/li/div[@class="publisher_info"][1]
    # //div[@class="bang_list_box"]/ul[@class="bang_list clearfix bang_list_mode"]/li/div[@class="price"]/p[1]/span[1]

    # li_list = soup.select('//div[@class="bang_list_box"]/ul[@class="bang_list clearfix bang_list_mode"]/li')

    div_list = soup.find_all('div', class_='bang_list_box')

    for div in div_list:
        print(div.find('ul', class_='bang_list clearfix bang_list_mode').li.div.text)

    # li_list = soup.find_all('/html/body/div[3]/div[3]/div[2]/ul/li')
    print(len(div_list))

    # for li in li_list:
    #     name = li.xpath('./div[@class="name"]').extract_first()
    #     print(name)


def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


if __name__ == "__main__":
    page = 2
    for i in range(1, page):
        url = 'https://bang.dangdang.com/books/fivestars/1-' + str(page)

        html = request_dandan(url)

        items = parse_result(html)

        for item in items:
            write_item_to_file(item)
