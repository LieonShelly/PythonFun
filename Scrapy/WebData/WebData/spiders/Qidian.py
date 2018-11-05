# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy import Request
from urllib.parse import urlencode
from WebData.items import BookItem
from WebData.items import ChapterItem
from WebData.items import ContentItem

class QidianSpider(Spider):
    name = 'Qidian'
    allowed_domains = ['www.qidian.com', 'book.qidian.com', 'read.qidian.com']
   
    def start_requests(self):
        # yield Request("https://read.qidian.com/chapter/8s7RmxQkntY3LbtcZNMchg2/fn_NgkMI2962uJcMpdsVgA2",callback=self.parseChapterContent)
        data = {"page": 1}
        maxPage = 100
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
                    img = li.css('.book-img-box').xpath('./a/@href').extract_first()
                    detailURI = li.css('.book-mid-info').xpath('./h4//a/@href').extract_first()
                    bookTitle = li.css('.book-mid-info').xpath('./h4/a/text()').extract_first()
                    intro =  li.css('.book-mid-info').css("p.intro::text").extract_first()
                    lastUpdateTitle = li.css('.book-mid-info').css('p.update::text').extract_first()
                    lastUpdateURI = li.css('.book-mid-info').css('p.update').xpath('./a/@href').extract_first()
                    catlog = "https:" + detailURI + "#Catalog"
                    bookItem = BookItem()
                    bookItem['detailURI'] = "https:" + detailURI 
                    bookItem['bookTitle'] = bookTitle
                    bookItem['intro'] = intro
                    yield bookItem
                    yield Request(catlog,callback=self.parseChapterList)


    def parseChapterList(self, response):
        divWrap = response.css("div.volume-wrap")
        for volume in divWrap:
            uls = volume.css("ul.cf")
            for ul in uls:
                chapterContentURIs = ul.xpath('./li/a/@href')
                chapterTitles = ul.xpath('./li/a/text()')
                for (chapterContentURI, chapterTitle) in zip(chapterContentURIs, chapterTitles):
                    content = "https:" + chapterContentURI.extract()
                    chapater = ChapterItem()
                    chapater['chapterContentURI'] = content
                    chapater['chapterTitle'] = chapterTitle.extract()
                    chapater['detailURI'] = response.url
                    yield chapater
                    yield Request(content,callback=self.parseChapterContent)

                
    def parseChapterContent(self, response):
        chapterURI = response.url 
        contents = response.css('div.read-content').xpath('./p/text()')
        contentStr = "".join(contents.extract()).replace('\u3000', "")
        content = ContentItem()
        content['content'] = contentStr
        content['chapterContentURI'] = chapterURI
        yield content
    

# 章节内容 https://read.qidian.com/chapter/j1uUFQtIDcYuTkiRw_sFYA2/j3uJh4HjyHn4p8iEw--PPw2
# 目录列表 https://book.qidian.com/info/1005269238#Catalog
# 书籍列表


