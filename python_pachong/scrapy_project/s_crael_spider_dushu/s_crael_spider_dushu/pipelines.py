# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings


class SCraelSpiderDushuPipeline:
    def open_spider(self,spider):
        self.fp = open('dushu.json','w',encoding='utf-8')
        print("-----------------------------------------")


    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    def close_spider(self,spider):
        self.fp.close()
        print('------------------------------------------')


class SCraelSpiderDushuPipelineSecond:

    '''
    DB_HOST = '10.10.224.185'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PASSWROD = '111111'
    DB_NAME = 'spider01'
    DB_CHARSET = 'utf8'
    '''

    def open_spider(self, spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWROD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

    def connect(self):
        self.conn = pymysql.connect(
                                    host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.password,
                                    db=self.name,
                                    charset=self.charset,
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        sql = 'insert into book(name,src) values ("{}","{}")'.format(item['name'],item['src'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()