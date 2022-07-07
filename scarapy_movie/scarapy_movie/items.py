# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScarapyMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # //div[@class="co_content8"]//td[1]//a[2]/text()
    name = scrapy.Field()
    # //div[@class="co_content8"]//td[1]//a[2]/@href
    src = scrapy.Field()
