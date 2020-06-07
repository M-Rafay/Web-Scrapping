# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonbooksItem


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    start_urls = ['https://www.amazon.com/gp/new-releases/books/?ie=UTF8&ref_=sv_b_2']

    def parse(self, response):
        items= AmazonbooksItem()
        all_product= response.css('.zg-item')

        for products in all_product:
            product_name=products.css('.p13n-sc-line-clamp-1::text').extract()
            product_author=products.css('.a-size-small::text').extract()
            product_price=products.css('.p13n-sc-price::text').extract()
            product_imagelink=products.css('img::attr(src)').extract()




            items['product_name']=product_name
            items['product_author'] =product_author
            items['product_price'] =product_price
            items['product_imagelink'] =product_imagelink

            yield items

            next_page = response.css('li.a-last a::attr(href)').get()

            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
            # yield {
            #     'product_name':product_name,
            #     'product_author':product_author,
            #     'product_price':product_price,
            # }

    # product_name=response.css('.p13n-sc-line-clamp-1::text').extract()
        # product_author=response.css('.a-link-child::text').extract()
        # product_price=response.css('.p13n-sc-price::text').extract()
        # product_imagelink=response.css('img::attr(src)').extract()
        #
        #
        # items['product_name']=product_name
        # items['product_author'] =product_author
        # items['product_price'] =product_price
        # items['product_imagelink'] =product_imagelink
        #
        # yield items

