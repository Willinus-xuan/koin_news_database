# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source_name = scrapy.Field()
    news_url = scrapy.Field()
    news_content = scrapy.Field()
    img_url = scrapy.Field()


