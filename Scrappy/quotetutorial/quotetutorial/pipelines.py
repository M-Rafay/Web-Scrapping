# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class QuotetutorialPipeline(object):
    def __init__(self):         #"__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology.
        self.create_connection()
        self.create_table()

    def create_connection(self):#this function is used to create table to the database or if already present it creates the connection to the database
        self.conn= sqlite3.connect('myquotes.db')
        self.curr= self.conn.cursor()
    def create_table(self):#this function is used to creat table and if already present then drop it and create new one
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                            title text,
                            author text,
                            tag text
                            )""")
    def store_db(self,items):#inserting values from items to the database table
        self.curr.execute("""insert into quotes_tb values (?,?,?)""", (
            items['title'][0],
            items['author'][0],
            items['tag'][0]

        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item) #calling function to store data in table
        return item
