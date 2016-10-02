import scrapy
from scrapy.http import Request
from twitterscraper import items
from twitterscraper.utils.project import parse_query
# from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from IPython.core.debugger import Tracer
import json
from scrapy.settings import default_settings

class FirstTweetSpider(scrapy.Spider):
    name = "firsttweet"
    allowed_domains = ["twitter.com"]
    # custom_settings = {}
    start_urls = []
    # settings = default_settings

    def __init__(self, domain=None, infile='yes_nurses.json'):
        self.url_string = 'https://discover.twitter.com/first-tweet#'
        with open(infile) as f:
            self.nurse_list = json.load(f)
        self.index = 0
        name = self.nurse_list[self.index]
        name = name[1:]
        self.start_urls.append(self.url_string + str(name))
        # Tracer()()

    def parse(self, response):
        filename = str(self.index) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        if (self.index < len(self.nurse_list)):
            self.index += 1
            next_name = self.nurse_list[self.index]
            next_url = self.url_string + str(next_name[1:])
            Tracer()()
            yield scrapy.Request(next_url, callback=self.parse)
