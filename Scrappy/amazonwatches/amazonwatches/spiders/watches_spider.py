import scrapy
from ..items import AmazonwatchesItem


class AmazonwatchesSpider(scrapy.Spider):
    name = 'watches'
    start_urls=[
        'https://www.amazon.com/s?bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A6358539011&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=554625a3-8de1-4fdc-8877-99874d353388&pf_rd_r=MFEY2MD07H86YC7AWBHM&pf_rd_s=merchandised-search-4&pf_rd_t=101&ref=s9_acss_bw_cts_AEMFVNEN_T3_w'
    ]

    def parse(self, response):
        items = AmazonwatchesItem()

        all_watches = response.css('div.s-border-bottom')
        for watches in all_watches:
            title = watches.css('.a-color-base.a-text-normal::text').extract()
            price = watches.css('.a-price-whole::text').extract()

            items['title'] = title
            items['price'] = price

            yield items
