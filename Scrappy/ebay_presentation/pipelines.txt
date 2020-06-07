# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class EbayPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn= sqlite3.connect('ebay.db')
        self.curr= self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS ebay_laptops""")
        self.curr.execute("""create table ebay_laptops(
                            title text,
                            price text,
                            image_link text
                            )""")
    def store_db(self,items):
        self.curr.execute("""insert into ebay_laptops values (?,?,?)""", (
            items['title'][0],
            items['price'][0],
            items['image_link'][0]

        ))
        self.conn.commit()


    def process_item(self, item, spider):
        self.store_db(item)
        return item
