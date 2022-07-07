import scrapy

from scarapy_movie.items import ScarapyMovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['m.dytt8.net']
    start_urls = ['https://m.dytt8.net/']

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//td[1]//a[2]')

        for a in a_list:
            # 获取第一页的地址和要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # print(name, href)

            # 第二页地址是
            url = 'https://m.dytt8.net/' + href
            print(name, url)

            # 对第二页链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        # //div[@id="Zoom"]/span/img/@src --> //div[@id="Zoom"]//img/@src
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()

        name = response.meta['name']

        movies = ScarapyMovieItem(src=src, name=name)

        yield movies
