# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:


import scrapy


class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
