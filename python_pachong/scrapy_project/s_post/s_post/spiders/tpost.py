import json
import scrapy

class TpostSpider(scrapy.Spider):
    name = "tpost"
    allowed_domains = ["fanyi.baidu.com"]

    # start_urls = ["https://fanyi.baidu.com/sug"]
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw':'spider'
        }

        yield scrapy.FormRequest(url = url,formdata=data,callback=self.parse_second)

    def parse_second(self,response):
        content = response.text
        obj = json.loads(content)
        print(obj)
