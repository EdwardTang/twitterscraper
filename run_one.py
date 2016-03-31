import os
import sys
import io
from twisted.internet import reactor
from twisted.internet import defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import logging
<<<<<<< HEAD
=======
# from scrapy.utils.log import configure_logging
>>>>>>> mongodb-branch
# from scrapy import signals
# from twitterscraper.spiders.search import SearchSpider

from IPython.core.debugger import Tracer

'''Loading the list of users' screen_name '''

<<<<<<< HEAD

runner = CrawlerRunner(get_project_settings())

q = 'echinacea'
d = runner.crawl('search', domain='twitter.com', query=q)
=======
# configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s',
# 	'LOG_FILE': 'logs/scrapy.log',
# 	'LOG_ENABLED': False
# 	}
# 	)
runner = CrawlerRunner(get_project_settings())

# q = 'valerian,lang:en,since:2006-03-21,until:2010-12-22'
# q = 'valerian,lang:en,since:2006-03-21,until:2007-04-12'
# q = '"st johns wort",lang:en,since:2006-03-21,until:2015-12-25'
q = 'from:kelsey3lisabeth,lang:en,since:2006-03-21,until:2016-02-27'
d = runner.crawl('test', domain='twitter.com', query=q)
>>>>>>> mongodb-branch

d.addBoth(lambda _: reactor.stop())
# log.msg('Reactor activated...')
# reactor.run()# the script will block here until all crawling jobs are finished
# log.msg('Reactor stopped.')
logging.log(logging.INFO,'Reactor activated...')
reactor.run()# the script will block here until all crawling jobs are finished
<<<<<<< HEAD
logging.log(logging.INFO,'Reactor stopped.')
=======
logging.log(logging.INFO,'Reactor stopped.')
>>>>>>> mongodb-branch
