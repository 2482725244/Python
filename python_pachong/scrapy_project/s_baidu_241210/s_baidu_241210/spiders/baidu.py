import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["sc.chinaz.com"]
    start_urls = ["https://sc.chinaz.com/tupian/24121029243.htm"]

    def parse(self, response):
        with open('qqa.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
