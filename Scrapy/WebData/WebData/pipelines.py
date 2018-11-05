# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
from WebData.settings import * 

class WebdataPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline():
        
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MysqlHost'),
            database=crawler.settings.get('MysqlDatabase'),
            user=crawler.settings.get('MysqlUser'),
            password=crawler.settings.get('MysqlPassword'),
            port=crawler.settings.get('MysqlPort')
        )
    
    def open_spider(self, spider):
        self.db = pymysql.connect("localhost", "root", "lieon1992316", "qidian", charset='utf8', port=3306)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    
    def process_item(self, item, spider):
        data = dict(item)
        keys = ",".join(data.keys())
        values = ",".join(['%s'] * len(data))
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (item.table, keys, values)
        insert = sql % tuple(data.values())
        self.cursor.execute(sql,tuple(data.values()))
        self.db.commit()
        return item

class MongoPipeline(object):
          
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
       

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=MongoUri,
            mongo_db=MongoDB
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    
    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item

