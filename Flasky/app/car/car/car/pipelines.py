# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import Request
from scrapy.exceptions import DropItem
# from scrapy.pipelines.images import ImagesPipeline

class CarPipeline(object):
    def process_item(self, item, spider):
        return item

class MongodPipeline(object):

    def __init__(self, mongod_uri, mongod_db):
        self.mongod_uri = mongod_uri
        self.mongod_db = mongod_db


    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongod_uri=crawler.settings.get('MONGO_URI'),
            mongod_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongod_uri)
        self.db = self.client[self.mongod_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
#
#
# class ImagePipeline(ImagesPipeline):
#
#     def file_path(self, request, response=None, info=None):
#         url = request.url
#         file_name = url.split('/')[-1]
#         return file_name
#
#     def item_completed(self, results, item, info):
#         image_paths =[x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem('Image Downloaded failed')
#         return item
#
#     def get_media_requests(self, item, info):
#         yield Request(item['url'])