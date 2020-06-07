import scrapy
from ..items import OlxmobileItem


class QuoteSpider(scrapy.Spider):
    name = 'mobiles'
    start_urls=[
        'https://www.olx.com.pk/mobile-phones_c1453?filter=make_eq_samsung'

    ]

    def parse(self, response):
        items = OlxmobileItem()
        all_div_quotes = response.css('li.EIR5N')
        for quotes in all_div_quotes:
            price = quotes.css('span._89yzn::text').extract()
            title = quotes.css('span._2tW1I::text').extract()
            seller = quotes.css('span.tjgMj::text').extract()

            items['price']=price
            items['title']=title
            items['seller']=seller
            yield items

            #     {
            #     'title': title,
            #     'author': author,
            #     'tag': tag
            # }

        # title = all_div_quotes.css('span.text::text').extract()
        # author=all_div_quotes.css('.author::text').extract()
        # tag=all_div_quotes.css('.tag::text').extract()
        # yield {
        #     'title' : title,
        #     'author' : author,
        #     'tag' : tag
        # }
