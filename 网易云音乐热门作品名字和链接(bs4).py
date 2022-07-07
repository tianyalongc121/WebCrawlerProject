import requests
from bs4 import BeautifulSoup


# from fake_useragent import UserAgent


class Wangyiyun(object):
    def __init__(self):
        self.base_url = 'https://music.163.com/discover/artist'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/102.0.0.0 '
                          'Safari/537.36 ',
            'referer': 'https://music.163.com/',
            'accept': 'text/html,application/xhtml+xml,application/xml;'
                      'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

    def get_xpath(self, url):
        res = requests.get(url, headers=self.headers)
        # print(res.text)
        html = res.text.replace('<适合才重要>', '适合才重要')
        return BeautifulSoup(html, 'html.parser')

    def singers_parse(self, url, items):
        html = self.get_xpath(url)
        song_dict = {}
        # a_lis = html.xpath('//div[@id="song-list-pre-cache"]/ul/li/a')  # "song-list-pre-cache"
        a_lis = html.find('div', attrs={'id': 'song-list-pre-cache'}).find('ul').find_all('li')
        for a in a_lis:
            song_name = a.find('a').get_text()
            print(song_name)
            # print(a)  # <li><a href="/song?id=1908417316">In The Shadow Of The Sun （我们终会相遇的，对吧）</a></li>
            song_url = 'https://music.163.com' + a.find('a').get('href')
            print(song_url)
            # song_dict[song_name] = song_url
        items['所有歌曲：'] = song_dict
        print(items)
        # name = items['歌手名：']
        # print(f'歌手：{name} 的歌曲已经获取完毕！即将写入文件！')
        # time.sleep(1)
        # self.writer_data(items)
        # print(f'歌手：{name} 的歌曲已经写入完毕！')


Wangyiyun().singers_parse(url='https://music.163.com/artist?id=50653542', items={})
