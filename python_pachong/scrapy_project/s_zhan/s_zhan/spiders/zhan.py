'''
    爬取站长素材前10页图片及介绍练习
'''
import scrapy
from fontTools.subset.svg import xpath
from matplotlib.pyplot import title

from ..items import SZhanItem


class ZhanSpider(scrapy.Spider):
    name = "zhan"
    allowed_domains = ["sc.chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/huacaotupian.html"]

    def parse(self, response):
        for i in range(1,11):
            origin_url = "https://sc.chinaz.com/tupian/huacaotupian.html"
            base_url = f'https://sc.chinaz.com/tupian/huacaotupian_{i}.html'
            if i == 1:
                yield scrapy.Request(url=origin_url, callback=self.parse_f, meta={'page': i})
            else:
                yield scrapy.Request(url=base_url, callback=self.parse_f, meta={'page': i})

    def parse_f(self, response):
        page = response.meta['page']
        url_list = response.xpath('//div[@class="item"]//img/@data-original').extract()
        title_list = response.xpath('//div[@class="item"]//img/@alt').extract()
        next_list = response.xpath('//div[@class="item"]//a/@href').extract()

        for i in range(len(next_list)):
            img_url = 'https:' + url_list[i]
            title = title_list[i]
            next_url = 'https://sc.chinaz.com' + next_list[i]

            yield scrapy.Request(url = next_url,callback=self.parse_s,meta={'img_url':img_url,'title':title,'page':page})


        # with open('aa.html','w',encoding='utf-8') as fp:
        #     fp.write(response.text)
        # print(img_url)

    def parse_s(self, response):
        page = response.meta['page']
        img_url = response.meta['img_url']
        title = response.meta['title']
        size = response.xpath('//div[@class="clearfix"][2]//span[2]/text()').extract_first()
        item = SZhanItem(img_url=img_url,title = title,size=size,page = page)

        yield item