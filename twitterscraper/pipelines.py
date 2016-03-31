# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from IPython.core.debugger import Tracer
import sys
import datetime
import traceback
import pymongo
<<<<<<< HEAD
=======
import re
>>>>>>> mongodb-branch
from pymongo import errors

from scrapy.exceptions import DropItem
from scrapy import settings
import logging

<<<<<<< HEAD
class MongoDBPipeline(object):
    def __init__(self):
        self.MONGODB_SERVER = "localhost"
        self.MONGODB_PORT = 27017
        self.MONGODB_DB = "tweets"


    @classmethod
    def from_crawler(cls, crawler):
        # return cls(
        #         MONGODB_SERVER=crawler.settings.get('MONGODB_SERVER', 'localhost')
        #         MONGODB_PORT=crawler.settings.get('MONGODB_PORT', 27017)
        #         MONGODB_DB=crawler.settings.get('MONGODB_DB', 'tweets')
        #     )
        cls.MONGODB_SERVER = crawler.settings.get('MONGODB_SERVER', 'localhost')
        cls.MONGODB_PORT = crawler.settings.getint('MONGODB_PORT', 27017)
        cls.MONGODB_DB = crawler.settings.get('MONGODB_DB', 'tweets')
        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def open_spider(self, spider):
        try:
            # Tracer()()
            self.client = pymongo.MongoClient(self.MONGODB_SERVER, self.MONGODB_PORT) 
            self.db = self.client[self.MONGODB_DB]
        except Exception as e:
            print self.style.ERROR("ERROR(MongodbPipeline): %s"%(str(e),))
            traceback.print_exc()

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        tweet_detail = {
            'tweet_id': item.get('tweet_id'),
            # 'convo_url': item.get('convo_url', ''),
            # 'is_retweet': item.get('is_retweet'),
            'user_id': item.get('user_id'),
            'user_screen_name': item.get('user_screen_name'),
            'text': item.get('text'),
            'created_at': item.get('created_at'),
            'image_url': item.get('image_url', []),
            'supplement': item.get('supplement',[]),
            'keyword': item.get('keyword', []),
            'num_retweets': item.get('num_retweets'),
            'num_favorites': item.get('num_retweets'),
            'update_time': datetime.datetime.utcnow(),
        }
        # collection_name = item.__class__.__name__
        '''
        Checking if record exists in MongoDB
        '''
        try:
            # Tracer()()
            result=self.db["tweet_detail"].insert(tweet_detail)
            item["mongodb_id"] = str(result)
            # Tracer()()
            # DuplicatesPipeline.ids_seen.add(item['tweet_id'])
            return item
        # except Exception as e:
        except errors.DuplicateKeyError as dke:
            raise DropItem("Duplicate item found: %s" % item)
            traceback.print_exc()
        except Exception as e:
            logging.log(logging.ERROR,"ERROR(MongodbPipeline): %s"%(str(e),) )   
            traceback.print_exc()

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['tweet_id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['tweet_id'])
            return item

# class DuplicatesPipeline(object):

#     def __init__(self):
#         self.ids_seen = set()

#     def process_item(self, item, spider):
#         if item['tweet_id'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['tweet_id'])
#             return item
=======
from scrapy_mongodb import MongoDBPipeline

class DuplicatesPipeline(MongoDBPipeline):

    def process_item(self, item, spider):
        # if the connection exists, don't save it
        matching_item = self.collection.find_one(
            {#'session_id': item['session_id'],
             'tweet_id': item['tweet_id'],
             # 'keyword': item['keyword'],
             'user_name': item['user_name']}
        )
        if matching_item is not None:
            # Tracer()()
            raise DropItem(
                "Duplicate found for %s, %s, %s" %
                (item['user_name'], item['tweet_id'],item['keyword'])
            )
        else:
            return item

class FilterNoContentPipeline(object):
    """Filter out tweet item that has no content in tweet

    """
    # def __init__(self, arg):
    #     super(FilterNoContentPipeline, self).__init__()
    #     self.arg = arg
    def process_item(self, item, spider):
        # Tracer()()
        if not item['text']:
            # Tracer()
            logging.log(logging.DEBUG, 'No content in the tweet: Drop tweet '+tweet['tweet_id'])
            raise DropItem(
                        "No content in tweet [%s] " % 
                        ( item['tweet_id'])
                        )
        return item

class FilterUserMentionPipeline(object):
    '''
    Filter out tweets that have target keyword in the user mentions within the text
    '''
    def __init__(self):
        self.twitter_username_re = re.compile(
                    r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z_]+[A-Za-z0-9_]+[A-Za-z]+[A-Za-z0-9])'
                    # r'(?<=@)\w+'
                    )
        self.query = {}

    def process_item(self, item, spider):           
        for op in item['query'].split(','):
            if len(op.split(':')) == 1:
                self.query['keyword'] = op.split(':')[0]
            else:
                self.query[op.split(':')[0]] = op.split(':')[1]
        # Tracer()()  
        if "keyword" in self.query.keys():
            user_mentions = self.twitter_username_re.match(item['text'])
            if user_mentions and any([self.query['keyword'].lower() in user_mention.lower() for user_mention in user_mentions.groups()]):
                # Tracer()()
                logging.log(logging.DEBUG, "Found %s in tweet [%s]  %s: Drop tweet [%s]" % 
                    (self.query['keyword'], item['tweet_id'], item['text'],item['tweet_id'])
                    )
                raise DropItem(
                    "Found %s in tweet [%s]  %s" % 
                    (self.query['keyword'], item['tweet_id'], item['text'])
                )
        return item
>>>>>>> mongodb-branch
