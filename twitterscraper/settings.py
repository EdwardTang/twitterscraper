# -*- coding: utf-8 -*-

# Scrapy settings for twitterscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'twitterscraper'

SPIDER_MODULES = ['twitterscraper.spiders']
NEWSPIDER_MODULE = 'twitterscraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = ''

# Configure maximum concurrent requests performed by Scrapy (default: 16)
<<<<<<< HEAD
CONCURRENT_REQUESTS=16
=======
CONCURRENT_REQUESTS=32
>>>>>>> mongodb-branch

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
<<<<<<< HEAD
DOWNLOAD_DELAY=6
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN=16
CONCURRENT_REQUESTS_PER_IP=16
=======
DOWNLOAD_DELAY=0.25
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN=16
CONCURRENT_REQUESTS_PER_IP=32
>>>>>>> mongodb-branch

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'twitterscraper.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'twitterscraper.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
<<<<<<< HEAD
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}
=======
# EXTENSIONS = {
#    # 'scrapy.telnet.TelnetConsole': None,
#    'twitterscraper.contrib.extension.spider_open_close_logging.SpiderOpenCloseLogging':500
# }
>>>>>>> mongodb-branch

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
<<<<<<< HEAD
   'twitterscraper.pipelines.MongoDBPipeline': 300,
   'twitterscraper.pipelines.DuplicatesPipeline': 250,
=======
   # 'twitterscraper.pipelines.CustomMongoDBPipeline': 300,
   'scrapy_mongodb.MongoDBPipeline':300,
   # 'twitterscraper.pipelines.MongoDBPipeline_test': 300,
   'twitterscraper.pipelines.DuplicatesPipeline': 250,
   # 
   'twitterscraper.pipelines.FilterNoContentPipeline': 150,
   'twitterscraper.pipelines.FilterUserMentionPipeline': 200,
>>>>>>> mongodb-branch
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
AUTOTHROTTLE_ENABLED=True
# The initial download delay
<<<<<<< HEAD
AUTOTHROTTLE_START_DELAY=3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG=False
AUTOTHROTTLE_CONCURRENCY_CHECK_PERIOD = 10#How many responses should pass to perform concurrency adjustments.
=======
AUTOTHROTTLE_START_DELAY=20.0
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY=60.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG=True
# AUTOTHROTTLE_CONCURRENCY_CHECK_PERIOD = 10#How many responses should pass to perform concurrency adjustments.
>>>>>>> mongodb-branch

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

# DOWNLOADER_MIDDLEWARES = {
#     'twitterscraper.contrib.downloadmiddleware.google_cache.GoogleCacheMiddleware':50,
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'twitterscraper.contrib.downloadmiddleware.rotate_useragent.RotateUserAgentMiddleware':400,
# }



# Retry many times since proxies often fail
<<<<<<< HEAD
RETRY_TIMES = 20
=======
RETRY_TIMES = 10
>>>>>>> mongodb-branch
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

DOWNLOADER_MIDDLEWARES = {
    # 'twitterscraper.contrib.downloadmiddleware.google_cache.GoogleCacheMiddleware':0,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'twitterscraper.contrib.downloadmiddleware.rotate_useragent.RotateUserAgentMiddleware':400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    # Fix path to this module
<<<<<<< HEAD
    # 'twitterscraper.contrib.downloadmiddleware.randomproxy.RandomProxy': 100,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}
=======
    'twitterscraper.contrib.downloadmiddleware.randomproxy.RandomProxy': 100,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}
DOWNLOAD_TIMEOUT = 20

>>>>>>> mongodb-branch

# DOWNLOADER_MIDDLEWARES = {
    # 'twitterscraper.contrib.downloadmiddleware.google_cache.GoogleCacheMiddleware':50,
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'twitterscraper.contrib.downloadmiddleware.rotate_useragent.RotateUserAgentMiddleware':400,
#     'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
#     # Fix path to this module
#     'twitterscraper.contrib.downloadermiddleware.randomproxy.RandomProxy': 100,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
# }

<<<<<<< HEAD
GOOGLE_CACHE_DOMAINS = ['twitter.com',]
=======
# GOOGLE_CACHE_DOMAINS = ['twitter.com',]
>>>>>>> mongodb-branch

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = '_reliable_list.txt'
<<<<<<< HEAD
USER_AGENT_LIST = "_user_agent_list.txt"
LOG_FILE = "logs/scrapy.log"
=======
PROXY_CHANGING_ODDS = 33

USER_AGENT_LIST = "_user_agent_list.txt"
USER_AGENT_CHANGING_ODDS = 60

LOG_FILE = "logs/scrapy.log"
LOG_ENABLED = False
>>>>>>> mongodb-branch

# scrapy-webdriver settings
# DOWNLOAD_HANDLERS = {
#     'http': 'scrapy_webdriver.download.WebdriverDownloadHandler',
#     'https': 'scrapy_webdriver.download.WebdriverDownloadHandler',
# }

# SPIDER_MIDDLEWARES = {
#     'scrapy_webdriver.middlewares.WebdriverSpiderMiddleware': 543,
# }

# WEBDRIVER_BROWSER = 'PhantomJS'  # Or any other from selenium.webdriver
                                 # or 'your_package.CustomWebdriverClass'
                                 # or an actual class instead of a string.

<<<<<<< HEAD
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "tweets"
MONGODB_COLLECTION = "tweet_detail"
=======
# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "tweets"
# MONGODB_COLLECTION = "tweet_detail"

# Basic configuration of scrapy-mongodb
# See http://sebdah.github.io/scrapy-mongodb/
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'tweets'
# MONGODB_COLLECTION = 'echinacea'
MONGODB_COLLECTION = 'tweet_detail_test'
MONGODB_ADD_TIMESTAMP = True
MONGODB_BUFFER_DATA = 10
>>>>>>> mongodb-branch
