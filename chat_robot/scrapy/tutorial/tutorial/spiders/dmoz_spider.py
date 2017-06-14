import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["zimuku.net"]
    start_urls = [
        "http://www.zimuku.net/search?q=&t=onlyst&ad=1&p=342"
    ]

    def parse(self, response):
        url = "http://shooter.zimuku.net/download/MjU2NjE0fENHLnJhcg%3D%3D"
        yield scrapy.Request(url, callback = self.parse_output)

    def parse_output(self, response):
        print("####################")
