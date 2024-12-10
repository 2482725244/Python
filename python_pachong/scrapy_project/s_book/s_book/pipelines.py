# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from traceback import print_tb

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SBookPipeline:
    def open_spider(self,spider):
        self.fp = open('xiaoshuo.json','w',encoding='utf-8')
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")



    def process_item(self, item, spider):
        self.fp.write(str(item))
        print('xieru')
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("bbbbbbbbbbbbbbbbbbbbb")

import urllib.request

class SBookPipelineSecond:

    def open_spider(self,spider):
        print("11111111aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    def process_item(self, item, spider):
        urllib.request.urlretrieve(item['img_url'],'books/'+f'第{item['page']}页'+item.get('name')+'.jpg')
        print("load over")
        # print(item)
        return item

    def close_spider(self, spider):
        print("2222222bbbbbbbbbbbbbbbbbbbbb")