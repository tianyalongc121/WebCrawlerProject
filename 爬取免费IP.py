# https://free.kuaidaili.com/free/inha/

# 网页分析:BeautifulSoup, PyQuery, xpath(lxml)

import requests
# from bs4 import BeautifulSoup
from lxml import etree


def create_request(page):
    url = 'https://free.kuaidaili.com/free/inha/' + str(page)
    # print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Host': 'free.kuaidaili.com'
    }

    response = requests.get(url, headers=headers)

    return response


def get_content(respose):
    content = respose.text
    # print(content)
    return content


def down_load(content):
    tree = etree.HTML(content)
    tr_list = tree.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

    for tr in tr_list:
        print(tr.find('data-title', "IP").text.strip())
        ip = tr.find('td[1]').text.strip()
        port = tr.find('td[2]').text.strip()
        # ip = tr.xpath('./td[@data-title="IP"]//text()')
        print(ip + ':' + port)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码: '))
    end_page = int(input('请输入结束页码: '))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        # 下载
        down_load(content)
