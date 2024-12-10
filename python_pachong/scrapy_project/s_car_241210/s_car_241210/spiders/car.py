import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/price"]

    def parse(self, response):
        name_list = response.xpath('//div[contains(@class,"tw-mt")]//a[@target="_blank"]/text()')
        price_list = response.xpath('//div[contains(@class,"tw-mt")]//p[contains(@class,"")]/text()')
        print("===================================================================")
        for i in range(len(name_list)):
            print(name_list[i],"-",price_list[i])
        print("===================================================================")
