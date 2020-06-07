# -*- coding: utf-8 -*-
import scrapy
from ..items import EbayItem


class EbayLaptopsSpider(scrapy.Spider):
    name = "ebaylaptops"
    #allowed_domains = ["ebay.com"]
    start_urls = ['https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276']

    def parse(self, response):
        items = EbayItem()
        all_laptops = response.css('.s-item')
        for laptops in all_laptops:
            title = laptops.css('.s-item__title::text').extract()
            price = laptops.css('.s-item__price::text').extract()
            image_link = laptops.css('.s-item__image-img::attr(src)').extract()

            items['title'] = title
            items['price'] = price
            items['image_link'] = image_link

            yield items
            # yield {
            #     'title' : title,
            #     'price' : price,
            #     'image_link' : image_link
            # }


