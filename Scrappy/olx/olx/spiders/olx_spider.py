import scrapy
from ..items import OlxItem

class OlxSpider(scrapy.Spider):
    name = 'olx'
    start_urls=[
        'https://www.olx.com.pk/toyota-cars_c84?filter=make_eq_toyota'

    ]

    def parse(self, response):
        items=OlxItem()
        all_div_quotes = response.css('div.IKo3_')
        for quotes in all_div_quotes:
            Price = quotes.css('span._89yzn::text').extract()
            Model = quotes.css('span._2TVI3::text').extract()
            Tag = quotes.css('span._2tW1I::text').extract()
            # yield {
            #     'Price': Price,
            #     'Model': Model,
            #     'Tag': Tag
            # }
            items['Price'] = Price
            items['Model'] = Model
            items['Tag'] = Tag
            yield items


            # next_page = response.css('li.next a::attr(href)').get()
            #
            # if next_page is not None:
            #     yield response.follow(next_page, callback=self.parse)


            # items = QuotetutorialItem()
            # all_div_quotes = response.css('div.quote')
            # for quotes in all_div_quotes:
            #     title = quotes.css('span.text::text').extract()
            #     author = quotes.css('.author::text').extract()
            #     tag = quotes.css('.tag::text').extract()
            #
            #     items['title'] = title
            #     items['author'] = author
            #     items['tag'] = tag
            #     yield items
            #
            # next_page = response.css('li.next a::attr(href)').get()

            # title = all_div_quotes.css('span._89yzn::text').extract()
        # author=all_div_quotes.css('span._2TVI3::text').extract()
        # tag=all_div_quotes.css('span._2tW1I::text').extract()
        # yield {
        #     'price' : title,
        #     'model' : author,
        #     'tag' : tag
        # }
        #
