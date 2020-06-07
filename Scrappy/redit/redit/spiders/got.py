# -*- coding: utf-8 -*-
import scrapy


class GotSpider(scrapy.Spider):
    name = 'got'
    # allowed_domains = ['redit.com']
    start_urls = ['https://www.reddit.com/r/gameofthrones/']

    def parse(self, response):
        # Extracting the content using css selectors
        titles = response.css('._eYtD2XCVieq6emjKBH3m::text').extract()
        votes = response.css('.FHCV02u6Cp2zYL0fhQPsO::text').extract()
        # times = response.css('._3jOxDPIQ0KaOWpzvSQo-1s::text').extract()
        # comments = response.css('._1rZYMD_4xY3gRcSS3p8ODO::text').extract()

        # Give the extracted content row wise
        for item in zip(titles,votes):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'vote': item[1]
                # 'created_at': item[2],
                # 'comments': item[3],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info

