# -*- coding: utf-8 -*-
import scrapy


class AmazonwatchesSpider(scrapy.Spider):
    name = 'amazonwatches'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A6358539011&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=554625a3-8de1-4fdc-8877-99874d353388&pf_rd_r=MFEY2MD07H86YC7AWBHM&pf_rd_s=merchandised-search-4&pf_rd_t=101&ref=s9_acss_bw_cts_AEMFVNEN_T3_w']

    def parse(self, response):
        def parse(self, response):
            # print("procesing:" + response.url)
            # Extract data using css selectors
            product_name = response.css('.a-size-base-plus.a-color-base.a-text-normal::text').extract()
            price_range = response.css('.a-price-whole::text').extract()
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

        pass
