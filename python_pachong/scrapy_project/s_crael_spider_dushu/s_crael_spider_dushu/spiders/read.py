import scrapy
import pymysql
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import SCraelSpiderDushuItem


class ReadSpider(CrawlSpider):
    name = "read"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1179_1.html"]

    rules = (Rule(LinkExtractor(allow=r"https://www.dushu.com/book/1179_\d+\.html"),
                                callback="parse_item",
                                follow=True),)

    def parse_item(self, response):
        name_list = response.xpath('//div[@class="book-info"]//h3//a/text()').extract()

        src_list = response.xpath('//div[@class="book-info"]//img/@data-original').extract()

        for i in range(len(name_list)):
            name = name_list[i]
            src  = src_list[i]
            book = SCraelSpiderDushuItem(name=name,src=src)
            yield book


        # item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
