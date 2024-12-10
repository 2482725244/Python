import scrapy

from ..items import SBookItem


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["www.qimao.com"]
    start_urls = ["https://www.qimao.com/shuku/a-a-a-a-a-a-a-click-1/"]


    # def parse(self, response):
    #     print("================================================================================================")
    #     for i in range(1,26):
    #         url = f'https://www.qimao.com/shuku/a-a-a-a-a-a-a-click-{i}/'
    #         yield scrapy.Request(url = url,callback=self.parse_f,meta={'page':i})
    #
    #     print("================================================================================================")



    def parse(self, response):
        with open('aa.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
        # page = response.meta.get('page')
        # print(page,response.url)
        li_list = response.xpath('//div[@class="qm-mod-tb"]//ul[contains(@class,"qm-pic")]//li')
        name_list = li_list.xpath('.//div[@class="txt"]//a/text()').extract()
        img_list = li_list.xpath('./div[@class="pic"]//img/@src').extract()
        next_list = li_list.xpath('./div[@class="pic"]/a/@href').extract()
        print("----->",next_list,li_list,name_list,img_list)

        for i in range(len(next_list)):
            print(i,name)
            url = 'https://www.qimao.com/'+next_list[i]
            name = name_list[i]
            img_url = img_list[i]
            yield scrapy.Request(url=url,callback=self.parse_second,meta={'name':name,'img_url':img_url,'page':page})

        # for i in range(len(name_list)):
        #     name = name_list[i]
        #     img_url = img_list[i]
        #
        #     book = SBookItem(name=name,img_url=img_url)
        #     yield book


    def parse_second(self,response):
        page = response.meta.get('page')
        print(response.url,page)
        score = response.xpath('//div[@class="wrap-txt"]//span[@class="score"]/text()')[0].extract()
        name = response.meta['name']
        img_url = response.meta.get('img_url')
        item = SBookItem(name=name,img_url=img_url,score=str(score)+'分',page = page)
        yield item
