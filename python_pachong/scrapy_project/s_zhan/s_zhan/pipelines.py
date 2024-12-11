# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SZhanPipeline:

    def open_spider(self,spoder):
        self.fp = open('zhan.json','w',encoding='utf-8')
        print('aaa')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self,spider):
        self.fp.close()
        print('bbbb')


import urllib.request
class SZhanPipelineSecond:

    def open_spider(self,spoder):
        print('aaa')

    def process_item(self, item, spider):
        page = item['page']
        save_point = 'ts/'+f'第{page}页'+item['title']+'.jpg'
        img_url = item['img_url']
        urllib.request.urlretrieve(img_url,save_point)
        return item

    def close_spider(self, spider):
        print('bbbb')
