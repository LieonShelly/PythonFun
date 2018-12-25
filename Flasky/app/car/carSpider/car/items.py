# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item
from scrapy import Field

class CarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CarBrand(Item):
    brand_id = Field()
    name = Field()
    letter = Field()
    logo = Field()

class CarSerial(Item):
    brandId = Field()
    brandName = Field()
    brandAllspell = Field()
    child = Field()

class CarSeialChildDetail(Item):
    # aerfaluomioustelvio
    allSpell = Field()
    # 2017款 2.0T 200HP 精英版
    yearCarList = Field()
    # 2.0升/149kW 涡轮增压
    configName = Field()

class NewCar(Item):
    brand_name = Field()
    serials = Field()

class NewCarSerialDetail(Item):
    car_serial_id = Field()
    car_lists = Field()

