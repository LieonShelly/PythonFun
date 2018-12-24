# -*- coding: utf-8 -*-
import scrapy
from  car.items import NewCar
import json
from urllib.parse import urlparse, parse_qs
from scrapy import Request

class NewcarSpider(scrapy.Spider):
    name = 'newcar'
    allowed_domains = ['auto.sohu.com', 'db.auto.sohu.com'] 
    start_urls = ['http://db.auto.sohu.com/zxauto-2004/5155'] # 
    # start_urls = ['http://db.auto.sohu.com/home/'] # http://db.auto.sohu.com/home/

    def start_requests(self):
        yield Request(url='http://db.auto.sohu.com/zxauto-2004/5155',callback=self.parse, meta={"use_selenium": True})

    def parse(self, response):
        tables = response.xpath('//div[@id="trm_data"]').css('.b').xpath('./table').css('.b')
        for table in tables:
            config_name = table.xpath('./thead/tr/th/text()').extract()[0]
            print(config_name)
        return
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
                    print(car_url)
                    yield Request(url=car_url,callback=self.parse_car)
                serial_json = {
                    "factory_title": factoryTitle,
                    "child_searials": child_searial
                  }
                serialsJson.append(serial_json)
            newCar['serials'] = serialsJson
            # yield newCar

    def parse_car(self, response):
        print(response.text)