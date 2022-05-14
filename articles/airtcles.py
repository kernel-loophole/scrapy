###################### Wikipedia aircle scraper #333####
from scrapy.linkextractors import LinkExtractor
from first_scraper.items import Article
from scrapy.spiders import Rule
from itertools import count
from scrapy.spiders import CrawlSpider
from stringcolor import *

from unicodedata import name
from django import urls
import scrapy

            
        

        # self.log(cs('I just visited: ',"red") + response.xpaht('//title/text()'))
        # self.logger.info("the respose is just arrive:",response.url)
class airtcles(scrapy.Spider):
    name="test_scrapy_1"
    
    start_urls=['https://en.wikipedia.org/wiki/Parsing',
              'https://docs.scrapy.org/en/latest/topics/commands.html#std-command-crawl',
              'https://en.wikipedia.org/wiki/Rectifier_(neural_networks)']
    #List of scrapy Rules
    #When multiple rules are in place, each link is checked
    #against the rules in order.
    rules=[Rule(LinkExtractor(allow='(/wiki/)'),callback='parse')]
    
    def parse(self, response):
        url=response.url
        print(cs(url,"orange"))
        title=response.css('h1::text').extract_first()
        lastUpdated = response.css('li#footer-info-lastmod'
'::text').extract_first()
        
        # lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        # lastUpdated = lastUpdated.replace('This page was last edited on ', '')
        print(cs("url:{0}".format(url),"red"))
        print(cs("file:{0}".format(title),"red"))
        print(cs("Last update{0}".format(lastUpdated),"blue"))
        
class item_airtcle(CrawlSpider):
    name = 'articleItems_1'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://kernel-loophole.github.io/This-Is-Hiader/']

    rules=[Rule(LinkExtractor(),callback='parse_items')]
    rules = [
     Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'),
     callback='parse_items', follow=True),
     ]
    def parse_items(self, response):
        link_list=list()
        article = Article()
        
        for i in response.css('a'):
            print(i)
            article['url'] = i
            link_list.append(i)
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@id=''"mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated'] = lastUpdated.replace('This page was '
        'last edited on ', '')
        return article 
        
    
