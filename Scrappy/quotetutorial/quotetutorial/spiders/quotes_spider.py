import scrapy   #this will help us to access allthe scrapy modules
from ..items import QuotetutorialItem     #importing class from items.py file
class QuoteSpider(scrapy.Spider):
    name = 'quotes'   #name of spider . we will use it to start crawler by using command in terminal : scrapy crawl quotes
    start_urls=[
        'http://quotes.toscrape.com/'       #the start_urls take the website links to be scraped

    ]

    def parse(self, response):  #parse allows to check the behaviour of different parts of the spider at the method level.
                                # It has the advantage of being flexible and simple to use, but does not allow debugging code inside a method.


        items = QuotetutorialItem()  #creating an "instance" of class "QuotetutorialItem" in "parse" function
        all_div_quotes = response.css('div.quote')  #“select” certain parts of the HTML document specified using css selector. We can also use xpath seletor.
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()         #it extract the data from span tag with "text" class ,
            author = quotes.css('.author::text').extract()          #it extract the data from  "author" class
            tag = quotes.css('.tag::text').extract()                #it extract the data from ".tag" class
                                                                    # "::text" is used to extract the data in the form of text.
            items['title']=title                    #collecting values into the Item Loader, typically using Selectors.
            items['author']=author                  #You can add more than one value to the same item field;
            items['tag']=tag                        #the Item Loader will know how to “join” those values later using a proper processing function.
            yield items                             # yield a Python dict with the extracted quote text and author

        next_page=response.css('li.next a::attr(href)').get()       #get the link of next page to be scraped

        if next_page is not None:                                   #check if page exist on the link or not
            yield response.follow(next_page, callback=self.parse)   #recursively follow the link to the next page

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
        # }\
