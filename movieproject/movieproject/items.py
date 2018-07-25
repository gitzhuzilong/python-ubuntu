# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    director = scrapy.Field()
    writer = scrapy.Field()
    actor = scrapy.Field()
    _type = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    release_date = scrapy.Field()
    duration = scrapy.Field()
    grade = scrapy.Field()
    introduce = scrapy.Field()
