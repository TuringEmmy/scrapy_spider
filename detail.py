# -*- coding: utf-8 -*-
import scrapy


class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['xxx']
    start_urls = ['http://xxx/']

    def parse(self, response):
        pass
