# -*- coding: utf-8 -*-
import scrapy
from ..items import ProjectNameItem  #importing class from items.py


class SpiderNameSpider(scrapy.Spider):
    name = "spider_name"  #used to typr crawl command
    #allowed_domains = ["example.com"]  #not required now
    start_urls = ['http://quotes.toscrape.com/']    #link of the web page which we want to scrap

    def parse(self, response):
        items=ProjectNameItem()     #creating instance

        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
        items['title'] = title
        items['author'] = author
        items['tag'] = tag
        yield items