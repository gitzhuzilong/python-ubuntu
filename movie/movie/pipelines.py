# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from scrapy.utils.project import get_project_settings
import pymongo


class MySqlPipeline(object):

    def __init__(self):
        settings = get_project_settings()
        host = settings['DB_HOST']
        port = settings['DB_PORT']
        user = settings['DB_USER']
        password = settings['DB_PASSWORD']
        dbname = settings['DB_NAME']
        dbcharset = settings['DB_CHARSET']
        self.conn = pymysql.Connect(host=host, port=port, user=user, password=password, db=dbname, charset=dbcharset)


    def process_item(self, item, spider):
        sql = 'insert into movie_table(post,name,score,_type,director,editor,actor,long_time,introduce) values("%s","%s","%s","%s","%s","%s","%s","%s","%s");' %(item['post'],item['name'],item['score'],item['_type'],item['director'],item['editor'],item['actor'],item['long_time'],item['introduce'])
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

class MyMongoDbPipeline(object):
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(host='127.0.0.1', port=27017)
        db = self.conn.movie
        self.collection = db.movie_col


    def process_item(self, item, spider):
        self.collection.insert(dict(item))

    def close_spider(self,spider):
        self.conn.close()



class MoviePipeline(object):
    def open_spider(self, spider):
        self.fp = open('movie.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()