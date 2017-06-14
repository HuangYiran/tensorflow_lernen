# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import chardet

class SubtitlePipeline(object):
    def process_item(self, item, spider):
        filename = item['filename']
        #file_name = url.replace('/', '_').replace(':', '_')
        fp = open('result/' + filename, 'wb')
        fp.write(item['body'])
        fp.close()
        return item
