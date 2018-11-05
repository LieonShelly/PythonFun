# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item
from scrapy import Field


class WebdataItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(Item):
    table = collection = "book"
    coverImage = Field()
    detailURI = Field()
    bookTitle = Field()
    intro = Field()

class ChapterItem(Item):
    table = collection = "chapter"
    detailURI = Field()
    chapterContentURI = Field()
    chapterTitle = Field()
    pass

class ContentItem(Item):
    table = collection = "content"
    content = Field()
    chapterContentURI = Field()
    bookId = Field()
    pass