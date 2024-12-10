import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["www.58.com"]
    start_urls = ["https://www.58.com/job/"]

    def parse(self, response):
        # print(response.body)
        a =  response.xpath('//h2/a[@href="/zhuanye/"]/text()')
        print(a.extract_first())