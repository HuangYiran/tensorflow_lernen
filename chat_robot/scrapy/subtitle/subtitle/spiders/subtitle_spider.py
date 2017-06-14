import scrapy
import sys
from w3lib.html import remove_tags
from subtitle.items import SubtitleItem


class SubTitleSpider(scrapy.Spider):
    name = "subtitle"
    allowed_domains = ["zimuku.net"]
    start_urls = [
        "http://www.zimuku.net/search?q=&t=onlyst&ad=1&p=" + str(i) for i in range(800, 900, 1)]
    print(start_urls)

    def parse(self, response):
        hrefs = response.selector.xpath('//div[contains(@class, "persub")]/h1/a/@href').extract()
        for href in hrefs:
            url = response.urljoin(href)
            request = scrapy.Request(url, callback = self.parse_detail)
            yield request

    def parse_detail(self, response):
        url = response.selector.xpath('//li[contains(@class, "dlsub")]/div/a/@href').extract()[0]
        print("processing: ", url)
        request = scrapy.Request(url, callback = self.parse_file)
        yield request

    def parse_file(self, response):
        print("#################")
        filename = response.headers['Content-Disposition'].decode('utf-8')
        filename = filename[30: -1]
        print(filename)
        print("#################")
        body = response.body
        item = SubtitleItem()
        item['filename'] = filename
        item['body'] = body
        return item
