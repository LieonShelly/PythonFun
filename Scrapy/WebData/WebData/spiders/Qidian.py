# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy import Request
from urllib.parse import urlencode

class QidianSpider(Spider):
    name = 'Qidian'
    allowed_domains = ['www.qidian.com']
   
    def start_requests(self):
        data = {"page": 1}
        maxPage = 10
        baseURL = "https://www.qidian.com/free/all?"
        for page in range(1, maxPage + 1):
            data["page"] = page
            url = baseURL + urlencode(data)
            yield Request(url=url)
        
    def parse(self, response):
        list = response.css("div.all-book-list")
        for item in list:
            uls = item.css('.book-img-text').xpath('./ul')
            for ul in uls:
                lis = ul.xpath('./li')
                for li in lis:
                   img =  li.css('.book-img-box').xpath('./a/@href').extract_first()
                   detailURI =  li.css('.book-mid-info').xpath('./h4//a/@href').extract_first()
                   bookTitle =  li.css('.book-mid-info').xpath('./h4/a/text()').extract_first()
                   intro =  li.css('.book-mid-info').css("p.intro::text").extract_first()
                   lastUpdateTitle = li.css('.book-mid-info').css('p.update::text').extract_first()
                   lastUpdateURI = li.css('.book-mid-info').css('p.update').xpath('./a/@href').extract_first()
                   print(img)




