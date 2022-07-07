"""
1. 请求地址的定制
2. 获取网页的源码
3. 下载

需求：下载前十页的图片
https://sc.chinaz.com/tupian/qinglvtupian_page.html
"""
import urllib.request
from lxml import etree


def create_request(p):
    if p == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(p) + '.html'
    # print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/102.0.0.0 '
                      'Safari/537.36 '
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    # print(len(name_list))
    # 一般设计图片的网站都会进行懒加载
    src_list = tree.xpath('//div[@id="container"]//a/img/@src')
    # print(len(name_list), len(src_list))

    for i in range(len(src_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        # print(name, url)
        urllib.request.urlretrieve(url=url, filename='./LoveImage/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码: '))
    end_page = int(input('请输入结束页码: '))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        # 下载
        down_load(content)
