# coding: utf-8
import scrapy

class ShareditorSpider(scrapy.Spider):
    name = 'shareditor'
    start_urls = ['http://www.shareditor.com/']

    def parse(self, response):
        for href in response.css('a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback = self.parse_question)
