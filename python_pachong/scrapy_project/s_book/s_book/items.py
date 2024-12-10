# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    img_url = scrapy.Field()
    name    = scrapy.Field()
    score   = scrapy.Field()
    page    = scrapy.Field()


