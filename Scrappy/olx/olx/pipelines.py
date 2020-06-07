# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class OlxPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn= sqlite3.connect('olx.db')
        self.curr= self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS cars_tb""")
        self.curr.execute("""create table cars_tb(
                            Price text,
                            Model text,
                            Tag text
                            )""")
    def store_db(self,items):
        self.curr.execute("""insert into cars_tb values (?,?,?)""",(
            items['Price'][0],
            items['Model'][0],
            items['Tag'][0]

        ))
        self.conn.commit()
    def process_item(self, item, spider):
        self.store_db(item)
        return item
