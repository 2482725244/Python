import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.qimao.com"]
    start_urls = ["https://www.qimao.com/shuku/a-a-a-a-a-a-a-click-1/"]

    def parse(self, response):
        with open('qq.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
