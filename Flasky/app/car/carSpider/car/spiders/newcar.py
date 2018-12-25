# -*- coding: utf-8 -*-
import scrapy
from  car.items import NewCar, NewCarSerialDetail
import json
from urllib.parse import urlparse, parse_qs
from scrapy import Request
import time

class NewcarSpider(scrapy.Spider):
    name = 'newcar'
    allowed_domains = ['auto.sohu.com', 'db.auto.sohu.com'] 
    start_urls = ['http://db.auto.sohu.com/home/'] # http://db.auto.sohu.com/home/

    # def start_requests(self):
    #     yield Request(url='http://db.auto.sohu.com/zxauto-2004/5155',callback=self.parse, meta={"use_selenium": True})

    def parse(self, response):
        brands = response.css('.close_child')
        for brand in brands:
            newCar = NewCar()
            title = brand.xpath('./h4/a/text()').extract()
            newCar['brand_name'] = title[1]
            serialsJson = []
            serials = brand.xpath('./ul').css('.tree_con')
            print("{}:{}".format(title[1], len(serials)))
            for serial in serials:
                factoryTitle = serial.xpath('./li').css('.con_tit').xpath('./a/text()').extract()
                factoryTitle = str(factoryTitle[1]).strip()
                serialCars = serial.xpath('./li/a').css('.model-a')
                child_searial = []
                for car in serialCars:
                    car_title = car.xpath('./text()').extract()
                    car_href = car.xpath('./@href').extract()
                    car_url = "http:" + car_href[0]
                    url = urlparse(car_url)
                    url_path = url.path
                    child_searial.append(
                            {
                                "child_searial_name": car_title[1],
                                "child_searial_id": url_path
                            }
                        )
                    yield Request(url=car_url, callback=self.parse_car)
                    time.sleep(1)
                serial_json = {
                    "factory_title": factoryTitle,
                    "child_searials": child_searial
                  }
                serialsJson.append(serial_json)
            newCar['serials'] = serialsJson
            # yield newCar

    def parse_car(self, response):
        tables = response.xpath('//div[@id="trm_data"]').css('.b').xpath('./table').css('.b')
        url_path = urlparse(response.url).path
        detail = NewCarSerialDetail()
        detail['car_serial_id'] = url_path
        car_lists = []
        for table in tables:
            generator_config = table.xpath('./thead/tr/th/text()').extract()[0]
            lists = table.xpath('./tbody/tr').css('.s_list')
            year_list = []
            for list in lists:
                year_name = list.xpath('./td').css('.ftdleft').xpath('./a/text()').extract()[0]
                guide_price = list.xpath('./td/a').css('.price1').xpath('./text()').extract()[0]
                s_price = list.xpath('./td/span/a').css('.acred').xpath('./text()').extract()
                if len(s_price) > 0:
                    s_price = str(s_price[0]).strip()
                else:
                    s_price = '暂无'
                print("year_name:{}, guide_price:{}, 4s_price:{}".format(year_name, guide_price, s_price))
                year_json = {
                    "year_name": year_name,
                    "guide_price": guide_price,
                    "price_4s": s_price
                }
                year_list.append(year_json)
            car_json = {
                "generator_config": generator_config,
                "year_list": year_list
            }
            car_lists.append(car_json)
        detail['car_lists'] = car_lists
        yield detail