import requests
from bs4 import BeautifulSoup

from lxml import etree


def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)

        soup = BeautifulSoup(r.text, "lxml")

        # tree = etree.HTML(r.text)
        # name_list = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
        # for name in name_list:
        #     print(name.text)

        div_list = soup.find_all('div', class_='info')
        for each in div_list:
            title = each.find('div', class_='hd').a.span.text.strip()
            info = each.find('div', class_='bd').p.text.strip()
            info = info.replace("\n", " ").replace("\xa0", " ")
            info = ' '.join(info.split())
            rating = each.find('span', class_='rating_num').text.strip()
            num_rating = each.find('div', class_='star').contents[7].text.strip()
            try:
                quote = each.find('span', class_='inq').text.strip()
            except:
                quote = ""
            movie_list.append([title, info, rating, num_rating, quote])
    return movie_list


movies = get_movies()
# for movie in movies:
    # print(movie)
