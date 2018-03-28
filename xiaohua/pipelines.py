# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import os
import urllib


class XiaohuaPipeline(object):

    def open_spider(self,spider):
        self.fp = open('hua.json','w',encoding='utf8')

    def process_item(self, item, spider):
        item_dict = dict(item)
        string = json.dumps(item_dict,ensure_ascii=False)
        self.fp.write(string+'\n')
        # 将图片下载到本地，如果有防盗链是保存不了的
        dirname = 'F:\data'
        filename = os.path.basename(item['image_url'])
        file_path = os.path.join(dirname,filename)
        urllib.request.urlretrieve(item['image_url'],file_path)
        return item

    def close_spider(self,spider):
        self.fp.close()

