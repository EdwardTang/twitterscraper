# -*- coding: utf-8 -*-
import time
import datetime
<<<<<<< HEAD
=======
import traceback
>>>>>>> mongodb-branch
from pprint import pprint
import urlparse
from urlparse import urlunparse
from urllib import urlencode
from urllib import urlopen
from urllib import quote
import json
import re
import random
# from random import random
from bisect import bisect
# from string import decode
from bs4 import BeautifulSoup
from collections import OrderedDict

# from scrapy.spider import BaseSpider
import scrapy
import logging
# from scrapy.spiders import Spider
# from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from twitterscraper import items
# from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from IPython.core.debugger import Tracer


class SearchSpider(scrapy.Spider):
    name = "search"
    allowed_domains = ["twitter.com"]
    start_urls = []
    min_tweet = None
    max_tweet = None
<<<<<<< HEAD
    settings = get_project_settings()

    def __init__(self, domain=None, query="from:TangTotoro"):
        # super(AdvSearchSpider, self).__init__(**kw)
        # query = kw.get('query') or 'from:purduetoday'
=======
    is_first_query = False
    data_max_position = ""
    settings = get_project_settings()

    def __init__(self, domain=None, query="from:TangTotoro"):
        # super(SearchSpider, self).__init__(*args, **kwargs)
        # query = kwargs.get('query')
        session_id = datetime.datetime.utcnow().date()
        
>>>>>>> mongodb-branch
        """
        Scrape items from twitter
        :param query:   Query to search Twitter with. Takes form of queries
        constructed with using Twitters
                        advanced search: https://twitter.com/search-advanced
        """
        self.query = query
<<<<<<< HEAD
=======
        self.query_keyword = query.split(',')[0]

        self.session_id = session_id.strftime('%Y-%m-%d')
        # Tracer()()
>>>>>>> mongodb-branch
        url = self.construct_url(self.query)
        # Tracer()()
        self.start_urls.append(url)

    def parse(self, response):
        # Random string is used to construct the XHR sent to twitter.com
        random_str = "BD1UO2FFu9QAAAAAAAAETAAAAAcAAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
<<<<<<< HEAD

        data = json.loads(response.body_as_unicode())
        #default rate delay is 12s
        rate_delay = self.settings['DOWNLOAD_DELAY']

        # delay_choices = [(1,30), (2,25), (3,20),(4,15),(5,10)]
        # delay_choices = [(1,50), (2,30), (3,10),(4,8),(5,2)] 
        delay_choices = [(1,90), (2,4), (3,3),(4,2),(5,1)]

        if data is not None and data['items_html'] is not None:
            tweets = self.extract_tweets(data['items_html'])
            # If we have no tweets, then we can break the loop early
            if len(tweets) == 0:
                Tracer()()
                # self.max_position = "TWEET-%s-%s-%s" % (self.max_tweet['tweet_id'], self.min_tweet['tweet_id'],random_str)
                # next_url = self.construct_url(self.query, max_position=self.max_position,operater="min_position")
                # Sleep for our rate_delay
                # time.sleep( random.uniform(0, self.settings['DOWNLOAD_DELAY']))
                pprint(data)
                logging.log(logging.DEBUG,data)
                logging.log(logging.INFO,
                    "Reach the end of search results( " + self.query + " )")
                return
                # yield Request(url=next_url, callback=self.parse)

            # If we haven't set our min tweet yet, set it now
            if self.min_tweet is None:
                self.min_tweet = tweets[0]
            elif self.min_tweet is not tweets[0]:
                self.min_tweet = tweets[0]

            # continue_search = self.save_tweets(tweets)

            # Our max tweet is the last tweet in the list
            self.max_tweet = tweets[-1]

            for tweet in tweets:
                # push parsed item to mongoDB pipline
                yield self.parse_tweet(tweet)

            if self.min_tweet['tweet_id'] is not self.max_tweet['tweet_id']:
                # Tracer()()
                self.max_position = "TWEET-%s-%s-%s" % (
                    self.max_tweet['tweet_id'],
                    self.min_tweet['tweet_id'],
                    random_str)
                # self.max_position = self.max_tweet['tweet_id']
                next_url = self.construct_url(
                    self.query,
                    max_position=self.max_position,
                    operater="max_position")
                # Sleep for our rate_delay
                # Tracer()()
                delay_multiple = self.weighted_choice(delay_choices)
                delay_time = random.uniform(rate_delay*(delay_multiple-1), rate_delay*delay_multiple)
                logging.log(logging.DEBUG,"Sleep for "+ str(delay_time) +" seconds")
                time.sleep(delay_time)               
                print
                print "Next Request:" + "TWEET-%s-%s" % (
                    self.max_tweet['tweet_id'], self.min_tweet['tweet_id'])
                print
                # Tracer()()
                yield Request(url=next_url, callback=self.parse)

    def weighted_choice(self,choices):
=======
        data = json.loads(response.body_as_unicode())
        #default rate delay is 12s
        # rate_delay = self.settings['DOWNLOAD_DELAY']
        # rate_delay = 2

        # delay_choices = [(1,30), (2,25), (3,20),(4,15),(5,10)]
        # delay_choices = [(1,50), (2,30), (3,10),(4,8),(5,2)] 
        # delay_choices = [(0,1),(1,89), (2,4), (3,3),(4,2),(5,1)]
        # delay_choices = [(1,60), (2,20), (3,10),(4,8),(5,2)]
        # delay_choices = [(0,33),(1,56), (2,5), (3,3),(4,2),(5,1)]
        # if data["max_position"] is not None:
            
        try:
            if data['items_html'] is not None:
                tweets = self.extract_tweets(data['items_html'])

                
                # If we have no tweets, then we can break the loop early
                if len(tweets) == 0 and data['has_more_items'] is False:
                    Tracer()()
                    pprint(data)
                    logging.log(logging.DEBUG, data)
                    logging.log(logging.INFO, "Reach the end of search results( " + self.query + " )")
                    return
                    # yield Request(url=next_url, callback=self.parse)

                for tweet in tweets:
                    # push parsed item to mongoDB pipline
                    yield self.parse_tweet(tweet, response)
                    
                # If we haven't set our min tweet yet, set it now
                if self.min_tweet is None:
                    self.is_first_query = True
                    self.min_tweet = tweets[0]
                elif self.min_tweet is not tweets[0]:
                    self.min_tweet = tweets[0]

                # continue_search = self.save_tweets(tweets)

                # The max tweet is the last tweet in the list
                self.max_tweet = tweets[-1]
                if self.min_tweet['tweet_id'] is not self.max_tweet['tweet_id']:
                    self.max_position = "TWEET-%s-%s-%s" % (
                        self.max_tweet['tweet_id'],
                        self.min_tweet['tweet_id'],
                        random_str)
                    # '''
                    #     is_first_query is a indicator used to identify the intial query. With the intial query 
                    #     the crwaler can simulate the hand-shake request while the delay time is greater than a 
                    #     predefined time period, for instance, 22 seconds
                    # '''
                    # if self.is_first_query:
                    #     self.data_max_position = self.max_position
                    #     self.is_first_query = False
                    # Construct next url to crawl
                    next_url = self.construct_url(
                        self.query,
                        max_position=self.max_position,
                        operater="max_position")

                    # Sleep for rate_delay
                    # Tracer()()
                    # delay_multiple = self.weighted_choice(delay_choices)
                    # if delay_multiple is not 0:
                    #     delay_time = random.uniform(rate_delay*(delay_multiple-1), rate_delay*delay_multiple)
                    #     logging.log(logging.DEBUG,"Sleep for "+ str(delay_time) +" seconds")
                    #     time.sleep(delay_time)
                    #     # if delay_time > 22:
                    #     #     next_url = self.construct_url(
                    #     #         self.query,
                    #     #         max_position=self.data_max_position,
                    #     #         operater="min_position")
                    #     #     yield Request(url=next_url, callback=self.parse,dont_filter=True)
                    # else:
                    #     logging.log(logging.DEBUG,"Sleep for 0 seconds")

                    print
                    print "Next Request:" + "TWEET-%s-%s" % (
                        self.max_tweet['tweet_id'], self.min_tweet['tweet_id'])
                    print
                    # Tracer()()
                    yield Request(url=next_url, callback=self.parse, dont_filter=True)
        except Exception, e:
            pass

    def weighted_choice(self, choices):
        """
        Random select weighted choices
        :param choices: The pair of values and weights
        :return: A weighted value
        """
>>>>>>> mongodb-branch
        # Tracer()()
        values, weights = zip(*choices)
        total = 0
        cum_weights = []
        for w in weights:
            total += w
            cum_weights.append(total)
        x = random.random() * total
        i = bisect(cum_weights, x)
        # Tracer()()
        return values[i]

<<<<<<< HEAD
    def parse_tweet(self, tweet):
        tweet_item = items.TwitterscraperItem()
=======


    def parse_tweet(self, tweet,response):
        tweet_item = items.TwitterscraperItem()
        tweet_item['session_id'] = self.session_id
>>>>>>> mongodb-branch
        tweet_item['tweet_id'] = tweet['tweet_id']
        tweet_item['text'] = tweet['text']
        tweet_item['user_id'] = tweet['user_id']
        tweet_item['user_screen_name'] = tweet['user_screen_name']
<<<<<<< HEAD
        tweet_item['created_at'] = tweet['created_at']
        # tweet_item['convo_url'] = tweet['convo_url']
        tweet_item['image_url'] = tweet['image_url']
        tweet_item['num_retweets'] = tweet['num_retweets']
        tweet_item['num_favorites'] = tweet['num_favorites']
        tweet_item['keyword'] = tweet['keyword']
        tweet_item['supplement'] = self.query
=======
        tweet_item['user_name'] = tweet['user_name']
        tweet_item['created_at_ts'] = tweet['created_at_ts']
        tweet_item['created_at_iso'] = tweet['created_at_iso']
        # tweet_item['convo_url'] = tweet['convo_url']
        # tweet_item['image_url'] = tweet['image_url']
        tweet_item['num_retweets'] = tweet['num_retweets']
        tweet_item['num_favorites'] = tweet['num_favorites']
        tweet_item['keyword'] = tweet['keyword']
        tweet_item['query'] = self.query
        # referring_url = response.request.headers.get('Referer', None)
        tweet_item['referring_url'] = response.request.headers.get('Referer', None) or self.start_urls[0]
        tweet_item['request_url'] = response.url
        tweet_item['quote_tweet_id'] = tweet['quote_tweet_userid']
        tweet_item['quote_tweet_userid'] = tweet['quote_tweet_userid']
        tweet_item['quote_tweet_username'] = tweet['quote_tweet_username']
        tweet_item['quote_tweet_screenname'] = tweet['quote_tweet_screenname']
        tweet_item['quote_tweet_text'] = tweet['quote_tweet_text']
        try:
            tweet_item['html'] = tweet['html']
        except Exception,e:
            Tracer()()
            pass
        # Tracer()()
>>>>>>> mongodb-branch
        return tweet_item

    def extract_tweets(self, items_html):
        """
        Parses Tweets from the given HTML
        :param items_html: The HTML block with tweets
        :return: A JSON list of tweets
        """
<<<<<<< HEAD
        soup = BeautifulSoup(items_html, "lxml")
        tweets = []
        for li in soup.find_all("li", class_='js-stream-item'):

            # If our li doesn't have a tweet-id, we skip it as it's not going
            # to be a tweet.
            if 'data-item-id' not in li.attrs:
                continue

            tweet = {
                'tweet_id': li['data-item-id'],
                'text': None,
                # 'is_retweet':false,
                'user_id': None,
                'user_screen_name': None,
                # 'user_name': None,
                'created_at': None,
                # 'convo_url': None,
                'image_url': [],
                'num_retweets': 0,
                'num_favorites': 0,
                'keyword': []
                }

            text_p = li.find("p", class_="tweet-text")
            if text_p is not None:
                # Replace each emoji with its unicode value
                # textElement.find('img.twitter-emoji').each((i, emoji) ->
                #   $(emoji).html $(emoji).attr('alt')
                # )
                # Tacer()()
                # pint
                # [rint(text_p)
                # emoji_dict = [
                #     emoji for emoji in text_p.find_all(
                #         "img", class_="twitter-emoji"
                #     )
                # ]
                # def replace_all(text, dic):
                #   for i, j in dic.iteritems():
                #       text = text.replace(i, j)
                #       return text
                # len(emoji_dict) is not 0:
                # for emoji in emoji_dict:
                #     Tracer()()
                    # text_p = text_p.replace(
                    #     str(emoji), emoji['alt'].decode('ascii')
                    #     )
                tweet['text'] = text_p.get_text()
                # print 'text_p.find("strong"):'+ str(type(text_p.find("strong")))
                # Tracer()()

                

                if text_p.find("strong"):
                    tweet['keyword'] = text_p.find("strong").get_text()               
            else:
                # Tracer()()
                continue
            # Tweet isRetweet
            # is_retweet = li.find('js-retweet-text').length is not 0

            # Tweet User ID, User Screen Name, User Name
            user_details_div = li.find("div", class_="tweet")
            if user_details_div is not None:
                tweet['user_id'] = user_details_div['data-user-id']
                tweet['user_screen_name'] = user_details_div[
                    'data-screen-name']
                # tweet['user_name'] = user_details_div['data-name']
                # Tracer()()
            # Tweet date
            date_span = li.find("span", class_="_timestamp")
            if date_span is not None:
                # tweet['created_at'] = float(date_span['data-time-ms'])
                tweet['created_at'] = int(date_span['data-time'])
                
            # Tweet conversation url
            # convo_a_tag = li.find("div",class_="stream-item-footer").find_next("a",class_="js-details")
            # if convo_a_tag is not None:
            #   print
            #   print "convo_a_tag:"+ str(convo_a_tag['href'])
            #   print
            # tweet['convo_url'] = str(convo_a_tag)

            # Tweet image url
            img_url_divs = li.select("div.js-old-photo")
            if len(img_url_divs) > 0:
                for img_url_div in img_url_divs:
                    tweet['image_url'].append(img_url_div['data-image-url'])

            # Tweet Retweets
            retweet_span = li.select(
                "span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount")
            if retweet_span is not None and len(retweet_span) > 0:
                tweet['num_retweets'] = int(
                    retweet_span[0]['data-tweet-stat-count'])

            # Tweet Favourites
            favorite_span = li.select(
                "span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount")
            if favorite_span is not None and len(retweet_span) > 0:
                tweet['num_favorites'] = int(
                    favorite_span[0]['data-tweet-stat-count'])

            # self.parse_tweet(tweet)
            # Tracer()()#break point
            try:
                # Tracer()()
                time_str = datetime.datetime.fromtimestamp(tweet["created_at"]).strftime('%Y-%m-%d %H:%M:%S')
                print
                print tweet['tweet_id'] + ': ' + time_str + ' ' + tweet['text']
                print
            except Exception, e:
                # Tracer()()
                print "ERROR(extract _timestamp): %s"%(str(e),)
            
            tweets.append(tweet)
        return tweets
=======
        try:
            soup = BeautifulSoup(items_html, "lxml")
            tweets = []
            twitter_username_re = re.compile(
                r'(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z_]+[A-Za-z0-9_]+[A-Za-z]+[A-Za-z0-9])'
                # r'(?<=@)\w+'
                )

            for li in soup.find_all("li", class_='js-stream-item'):
                # Tracer()()
                # If our li doesn't have a tweet-id, we skip it as it's not going
                # to be a tweet.
                if 'data-item-id' not in li.attrs:
                    continue

                tweet = {
                    'tweet_id': li['data-item-id'],
                    'text': None,
                    # 'is_retweet':false,
                    'user_id': None,
                    'user_screen_name': None,
                    'user_name': None,
                    'created_at_ts': None,
                    'created_at_iso': None,
                    # 'convo_url': None,
                    # 'image_url': [],
                    'num_retweets': 0,
                    'num_favorites': 0,
                    'keyword': [],
                    'quote_tweet_id':None,
                    'quote_tweet_userid':None,
                    'quote_tweet_username' :None,
                    'quote_tweet_screenname' :None,
                    'quote_tweet_text' :None,
                    'html':None
                    }
                try:
                    tweet['html'] = str(li)
                except Exception,e:
                    Tracer()()
                    pass

                '''
                Extract tweet text
                '''
                try:
                    text_p = li.find("p", class_="tweet-text")
                    if text_p is not None:
                        # Replace each emoji with its unicode value
                        # textElement.find('img.twitter-emoji').each((i, emoji) ->
                        #   $(emoji).html $(emoji).attr('alt')
                        # )
                        # Tacer()()
                        # pint
                        # [rint(text_p)
                        # emoji_dict = [
                        #     emoji for emoji in text_p.find_all(
                        #         "img", class_="twitter-emoji"
                        #     )
                        # ]
                        # def replace_all(text, dic):
                        #   for i, j in dic.iteritems():
                        #       text = text.replace(i, j)
                        #       return text
                        # len(emoji_dict) is not 0:
                        # for emoji in emoji_dict:
                        #     Tracer()()
                            # text_p = text_p.replace(
                            #     str(emoji), emoji['alt'].decode('ascii')
                            #     )
                        tweet['text'] = text_p.get_text()               

                        # If there is any user mention containing the query, then pass the tweet.
                        # Tracer()()
                        # if self.query.find("from:") == -1:
                        user_mentions = twitter_username_re.match(tweet['text'])
                        if user_mentions and any([self.query_keyword.lower() in user_mention.lower() for user_mention in user_mentions.groups()]):
                            # Tracer()()
                            logging.log(logging.DEBUG, 'Found '+self.query_keyword+' in '+ str(user_mentions.groups())+': Drop tweet '+tweet['tweet_id'])
                            continue
                        # If the keyword was found in the text and was the same with query, then accept the tweet 
                        # elif text_p.find("strong") and text_p.find("strong").get_text().lower() == self.query_keyword.lower():
                        #     tweet['keyword'] = text_p.find("strong").get_text()
                        # elif tweet['text'].lower().find(self.query_keyword.lower()) != -1:
                        #     tweet['keyword'] = self.query_keyword
                        # else:
                        #     # The keyword is not in the text, then pass the tweet.
                        #     # Tracer()()
                        #     logging.log(logging.DEBUG, 'No '+self.query_keyword +' in the content of tweet'+': Drop tweet '+tweet['tweet_id'])
                        #     continue                   
                    else:
                        # Tracer()()
                        logging.log(logging.DEBUG, 'No content in the tweet'+': Drop tweet '+tweet['tweet_id'])
                        continue
                except Exception, e:
                    Tracer()()
                    logging.log(logging.DEBUG, "ERROR(extract_text_p): %s"%(str(e),))
                    traceback.print_exc()
                '''
                Extract quote tweet content if exists
                '''
                try:
                    quote_tweet = li.find("div", class_="QuoteTweet-innerContainer")
                    if quote_tweet is not None:
                        # Tracer()()
                        tweet['quote_tweet_id'] = quote_tweet['data-item-id']
                        tweet['quote_tweet_userid'] = quote_tweet['data-user-id']
                        tweet['quote_tweet_screenname'] = quote_tweet['data-screen-name']
                        tweet['quote_tweet_username'] = quote_tweet.find("b",class_="QuoteTweet-fullname").get_text()
                        tweet['quote_tweet_text'] = quote_tweet.find("div",class_="QuoteTweet-text").get_text()
                except Exception, e:
                    Tracer()()
                    logging.log(logging.DEBUG, "ERROR(extract_quote_tweet): %s"%(str(e),))
                    traceback.print_exc()

                # Tweet isRetweet
                # is_retweet = li.find('js-retweet-text').length is not 0

                # Tweet User ID, User Screen Name, User Name
                try:
                    user_details_div = li.find("div", class_="tweet")
                    if user_details_div is not None:
                        tweet['user_id'] = user_details_div['data-user-id']
                        tweet['user_screen_name'] = user_details_div[
                            'data-screen-name']
                        tweet['user_name'] = user_details_div['data-name']
                        # Tracer()()
                    # Tweet date
                    date_span = li.find("span", class_="_timestamp")
                    if date_span is not None:
                        # tweet['created_at'] = float(date_span['data-time-ms'])
                        tweet['created_at_ts'] = int(date_span['data-time'])
                        try:
                            # tweet['created_at_iso'] = datetime.datetime.fromtimestamp(tweet["created_at_ts"]).strftime('%Y-%m-%d %H:%M:%S')
                            tweet['created_at_iso'] = datetime.datetime.fromtimestamp(tweet["created_at_ts"]).isoformat(' ')
                        except Exception, e:
                            Tracer()()
                            logging.log(logging.DEBUG, "ERROR(extract _timestamp): %s"%(str(e),)) 
                            traceback.print_exc()

                    # Tweet Retweets
                    retweet_span = li.select(
                        "span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount")
                    if retweet_span is not None and len(retweet_span) > 0:
                        tweet['num_retweets'] = int(
                            retweet_span[0]['data-tweet-stat-count'])

                    # Tweet Favourites
                    favorite_span = li.select(
                        "span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount")
                    if favorite_span is not None and len(retweet_span) > 0:
                        tweet['num_favorites'] = int(
                            favorite_span[0]['data-tweet-stat-count'])
                except Exception, e:
                    Tracer()()
                    logging.log(logging.DEBUG, "ERROR(extract_tweet_meta_data): %s"%(str(e),))
                    traceback.print_exc()

                # self.parse_tweet(tweet)
                # Tracer()()#break point
                
                print
                print tweet['tweet_id']+': '+tweet['created_at_iso']+' '+'['+tweet['user_name']+']'+' '+tweet['text']
                print
                

                tweets.append(tweet)
            return tweets
        except Exception, e:
            Tracer()()
            logging.log(logging.DEBUG, "ERROR(extract_tweets): %s"%(str(e),))
            traceback.print_exc()
>>>>>>> mongodb-branch

    @staticmethod
    def construct_url(query, max_position=None, operater="max_position"):
        """
        For a given query, will construct a URL to search Twitter with
        :param query: The query term used to search twitter
        :param max_position: The max_position value to select the next
        pagination of tweets
        :return: A string URL
        """
<<<<<<< HEAD

        params = {
            'vertical': 'default',
            # Query Param
            'q': query+ ' '+'lang:en'+' '+ 'since:2006-03-21 until:2013-01-20',
            # Type Param
            'src': 'typd'
=======
        sequent_q = ' '.join(query.split(','))
        # Tracer()()
        params = {
            'vertical': 'default',
            # Query Param
            # 'q': query+ ' '+'lang:en'+' '+'since:2007-01-19 until:2014-03-13', #st.john's wort since:2007-01-20 until:2014-03-12 
            'q': sequent_q,
            # Type Param
            'src': 'typd',
            'f':'tweets'
>>>>>>> mongodb-branch
        }

        #todo develop a query operator recognize function
        # def doit(text):
        #     import re
        #     matches=re.findall(r'\"(.+?)\"',text)
        #     # matches is now ['String 1', 'String 2', 'String3']
        #     return ",".join(matches)

        # q = doit(query) 

        # params = {
        #     'vertical': 'default',            
        #     # Type Param
        #     'src': 'typd'
        # }

        # If our max_position param is not None, we add it to the parameters
        if operater == "max_position":
            if max_position is not None:
                params['include_available_features'] = '1'
                params['include_entities'] = '1'
                params['max_position'] = max_position
                params['reset_error_state'] = 'false'

        elif operater == "min_position":
            if max_position is not None:
                params['composed_count'] = '0'
                params['include_available_features'] = '1'
                params['include_entities'] = '1'
                params['include_new_items_bar'] = 'true'
                params['interval'] = '30000'
                params['latent_count'] = '0'
                params['min_position'] = max_position
        # url_tupple = ('https', 'twitter.com', '/i/search/timeline',
        #               '', urlencode(OrderedDict(params)), '')
        url_tupple = ['https', 'twitter.com', '/i/search/timeline',
                      '', urlencode(OrderedDict(params)), '']
        # Tracer()()
        # url_tupple = ('https', 'twitter.com', 'i/profiles/show/'+user_screen_name+'/timeline/with_replies', '', urlencode(params), '')
        return urlunparse(url_tupple)
        # print urlunparse(url_tupple)
