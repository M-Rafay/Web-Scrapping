# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#extract data ->temporary container (items) -> store in data base
import scrapy



class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title=scrapy.Field()        #field is A dictionary containing all declared fields for this Item, not only those populated.
    author = scrapy.Field()     #The keys are the field names and the values are the Field objects used in the Item declaration.
    tag = scrapy.Field()
    # pass
