# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class AmazonbooksPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn= sqlite3.connect('amazon_books.db')
        self.curr= self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS books_tb""")
        self.curr.execute("""create table books_tb(
                            product_name text,
                            product_author text,
                            product_price text,
                            product_imagelink text
                            )""")
    def store_db(self,items):
        self.curr.execute("""insert into books_tb values (?,?,?,?)""",(
            items['product_name'][0],
            items['product_author'][0],
            items['product_price'][0],
            items['product_imagelink'][0]

        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
