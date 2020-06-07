# -*- coding: utf-8 -*-
import scrapy


class AliexpressTabletsSpider(scrapy.Spider):
    name = 'aliexpress_tablets'
    # allowed_domains = ['aliexpress.com']
    start_urls = ['https://www.aliexpress.com/category/200216607/tablet.html?switch_new_app=y'
                  # 'https://www.aliexpress.com/category/200216607/tablets/2.html?site=glo&g=y&tag=']
    ]
    def parse(self, response):
        # print("procesing:" + response.url)
        # Extract data using css selectors
        product_name = response.css('.item-title::text').extract()
        price_range = response.css('.price-current::text').extract()
        # Extract data using xpath
        # orders = response.xpath("//span[@class='shipping-value']/text()").extract()
        # company_name = response.xpath("//a[@class='store-name']/text()").extract()

        row_data = zip(product_name, price_range)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                # 'page': response.url,
                'product_name': item[0],
            # item[0] means product in the list and so on, index tells what value to assign
                'price_range': item[1]

            }

            # yield or give the scraped info to scrapy
            yield scraped_info