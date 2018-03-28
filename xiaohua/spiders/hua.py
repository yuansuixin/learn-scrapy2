# -*- coding: utf-8 -*-
import scrapy
from xiaohua.items import XiaohuaItem

class HuaSpider(scrapy.Spider):
    name = 'hua'
    allowed_domains = ['http://www.521609.com/']
    start_urls = ['http://www.521609.com/daxuexiaohua/']

    #保存要爬取的page页面
    page = 1
    url = 'http://www.521609.com/daxuexiaohua/list3'

    def parse(self, response):
        li_list = response.xpath("//div[@class="index_img list_center"]/ul/li")
        for li in li_list:
            item = XiaohuaItem()
            name = li.xpath('.//img/@alt').extract_first()
            image_url = 'http://www.521609.com/'+li.xpath('.//img/@src').extract_first()
            print(name)
            print(image_url)
            item['name'] = name
            item['image_url'] = image_url
            print(item)
            yield item

        self.page+=1
        if self.page<=10:
            url = self.url+str(self.page)+'.html'
            yield scrapy.Request(url=url,callback=self.parse)




