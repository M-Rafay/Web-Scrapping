# -*- coding: utf-8 -*-
import scrapy


class Practice1SpiderSpider(scrapy.Spider):
    name = 'practice1_spider'
    start_urls = ['https://www.aliexpress.com/category/200000600/men-belts.html?switch_new_app=y']

    def parse(self, response):
       
        title = response.css('a.item-title::text').extract()
        author=response.css('span.price-current::text').extract()
        tag=response.css('span.shipping-value::text').extract()
        yield {
            'title' : title,
            'author' : author,
            'tag' : tag
        }

        
