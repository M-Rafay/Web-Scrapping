# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ProjectNamePipeline(object):
    def __init__(self):
        self.create_connection()    #calling a function to create a connection to the database
        self.create_table()         #calling the function to create table in database

    def create_connection(self):
        self.conn= sqlite3.connect('myquotes.db')   #connect to databse or create new one if already present
        self.curr= self.conn.cursor()               #allow to work on database
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""") #delete table if already exist
        self.curr.execute("""create table quotes_tb(            
                            title text,
                            author text,
                            tag text
                            )""")   #create table
    def store_db(self,items):
        self.curr.execute("""insert into quotes_tb values (?,?,?)""",(
            items['title'][0],
            items['author'][0],
            items['tag'][0]

        ))  #insert values from items ti databse
        self.conn.commit()
    def process_item(self, item, spider):
        self.store_db(item) #calling function to store the data in database
        return item
