from fileinput import filename
from itertools import count
import string
from stringcolor import *
from typing import final
from unicodedata import name
from django import urls
import scrapy
# classes are spider, item, and fields
class Spider(scrapy.Spider):
    #name: identifies the Spider. It must be unique within a project, that is, you can’t set the same name for different
       #Spiders.
    name = "spider"
    def start_requests(self):
    
        start_urls = ['http://quotes.toscrape.com/page/1/',


        'http://kernel-loophole.github.io/This-Is-Hiader/',]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        page=response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
            
        

class get_it(scrapy.Spider):
# Name of spider to run
# example : scrapy crawl get_it

    name="get_it"
    def start_requests(self):

        urls=['http://flexstudent.nu.edu.pk']
        for i in urls:
            yield scrapy.Request(url=i,callback=self.parse)
    def parse(self, response):
        page=response.url.split("/")
        filename = f'{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
class make_it(scrapy.Spider):
    name="make_it"
    start_urls=['http://quotes.toscrape.com']
    def parse(self, response):
        page=response.url.split("/")
        filename = f'{page}.pdf'
        for i in response.css('a').getall():
            print(cs("LINK","red"),i)
          
            yield response.follow(i,callback=self.parse)
           
            
        self.log(f'Saved file {filename}')
        
        # for q in response.css('div.quote'):
        #     yield {
        #         'text':q.css('span.text::text').get(),
        #         'author':q.css('small.author::text').get(),
        #         'tags':q.css('div.tags a.tag::text').getall(),
        #     }
        print(cs("LINK","red"),count)
class l(scrapy.Spider):
    name="l"
    urls=['http://slate.nu.edu.pk/']
    def parse(self, response):
    
        for i in self.link_extractor(response):
            yield response.follow(i,callback=self.parse)
            
            print(cs("====>","red"),i)
        # self.log(cs('I just visited: ',"red") + response.xpaht('//title/text()'))
        # self.logger.info("the respose is just arrive:",response.url)