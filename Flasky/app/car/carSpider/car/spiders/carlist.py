# -*- coding: utf-8 -*-
import scrapy
from  car.items import CarBrand, CarSerial, CarSeialChildDetail
import random
from scrapy import Request
import json
import time
from urllib.parse import urlparse, parse_qs

class CarlistSpider(scrapy.Spider):
    name = 'carlist'
    start_urls = ['http://car.m.yiche.com/brandlist.html']
    serial_url = "http://api.car.bitauto.com/CarInfo/GetCarDataJson.ashx?action=serial&pid={pid}&datatype=1"
    serial_detail_url = "http://car.m.yiche.com/{Allspell}"


    def parse(self, response):
        lists = response.css(".brand-list")
        for list in lists:
            letters = list.css(".tt-small")
            boxs = list.css(".box")
            for index in range(0, len(boxs)):
                box = boxs[index]
                letter = letters[index].xpath("./span/text()").extract_first()
                names = box.xpath("./ul/li/a/span").css(".brand-name").xpath("./text()").extract()
                logos = box.xpath("./ul/li/a/span").css(".brand-logo").xpath("./img/@data-original").extract()
                logo_srcs = box.xpath("./ul/li/a/span").css(".brand-logo").xpath("./img/@src").extract()
                pids =  box.xpath("./ul/li/a/@data-id")
                print(len(pids))
                index = 0
                for (name, pid) in zip(names, pids):
                    brand = CarBrand()
                    brand['name'] = name
                    brand['letter'] = letter
                    # if index < len(logos):
                    #     brand['logo'] = logos[index]
                    brand_id = pid.extract()
                    brand['brand_id'] = brand_id
                    index = index + 1
                    yield brand
                    url = self.serial_url.format(pid=brand_id)
                    yield  Request(url=url,callback=self.parse_serial)
                # for(name, logo) in zip(names, logo_srcs):
                #      print("name:{name}, logo:{logo}".format(name=name, logo=logo))
                #      print("=====")
                #      brand = CarBrand()
                #      brand['name'] = name
                #      brand['letter'] = letter
                #      brand['logo'] = logo
                #      brand_id = random.randint(1, 5000)
                #      brand['brand_id'] = brand_id
                #      yield brand
                #
                for (name, logo) in zip(names, logos):
                    brand = CarBrand()
                    brand['name'] = name
                    brand['letter'] = letter
                    brand['logo'] = logo
                    brand_id = random.randint(1, 5000)
                    brand['brand_id'] = brand_id
                    yield brand

    def parse_serial(self, response):
        parse_result = urlparse(response.url)
        pid = parse_qs(parse_result.query)['pid'][0]
        json_array = json.loads(response.text)
        for obj in json_array:
            serial = CarSerial()
            serial['brandId'] = pid
            serial['brandName'] = obj['BrandName']
            serial['brandAllspell'] = obj['BrandAllspell']
            serial['child'] = obj['Child']
            yield  serial
            child_array = obj['Child']
            for child in child_array:
                allSpell = child['Allspell']
                yield Request(url=self.serial_detail_url.format(Allspell=allSpell),callback=self.parese_serial_detail,meta={"use_selenium": True})

    def parese_serial_detail(self, response):
        parse_result = urlparse(response.url)
        path = parse_result.path
        allSpell = path[1: len(path) - 1]
        item = CarSeialChildDetail()
        item['allSpell'] = allSpell
        configNames = response.xpath("//div[@id='yearDiv0']/div[@class='tt-small']/span/text()").extract()
        carLists = response.xpath("//div[@id='yearDiv0']/div[@class='car-card']")
        for index in range(0, len(configNames)):
            configName = configNames[index]
            item['configName'] = configName
            yearList = []
            print(configName)
            carlist = carLists[index]
            yearname = carlist.xpath('./ul/li/a/h2/text()').extract()
            price = carlist.xpath('./ul/li/a/dl/dt/text()').extract()
            for (year, price) in zip(yearname, price):
                year_json = {
                   'year_name': year,
                    'price': price
                }
                yearList.append(year_json)
            item['yearCarList'] = yearList
            yield  item
