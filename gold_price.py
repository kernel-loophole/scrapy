from cgi import print_environ
from faulthandler import disable
import chompjs
from fileinput import filename
import imghdr
import logging
from re import X
from tokenize import Name
from django import urls
from scrapy import *
import scrapy
from sqlalchemy import false
from stringcolor import *
class SecondSpider(Spider):
    name = 'second'
    start_urls = ['https://www.thenews.com.pk/']
    def make(response):
        x=response.xpath('//div[@id="content_left"]/div[@class="result c-container "]/h3/a/text()').extract()
        yield x
    def parse(self, response):
        logging.getLogger('scrapy').propagate = False
        m = '.heading-cat'
        counter=0
        for test in response.css(m):
            Name_SELECTOR = 'h2::text'
            counter+=1
            x=yield {
                counter: test.css(Name_SELECTOR).extract_first(),
            }
            print(cs('Head Line #====',"red"),counter)
            print(cs(test.css(Name_SELECTOR).extract_first(),"yellow"),)
        print(cs("Total","red"),counter)
class gold(Spider):
    name="gold"
    start_urls=['https://www.kitco.com/']
    def parse(self,response):
        logging.getLogger('scrapy').propagate = False
        m = '.item_title_info'
        l='.alternating'
        counter=0
        for test in response.css(l):
            Name_SELECTOR = 'td::text'
            counter+=1
            x=yield {
                counter: test.css(Name_SELECTOR).extract_first(),
            }
            print(cs('item name #====',"red"),counter)
            print(cs(test.css(Name_SELECTOR).extract_first(),"yellow"),)
        print(cs("Total","red"),counter)
class seconde(Spider):
    name="seconde"
    start_urls=['https://www.thenews.com.pk/']
    def parse(self,response):
    #link extarct
        x=yield{
            "link":response.css('a::attr(href)').getall(),
        }
        print(cs("link","red"),x)
        # for i in response.css("a::attr(href)"):
        #     x=yield 
        #     {
        #        "link": i.css("a::attr(href)").getall()
        #     }
        #     print(cs("Total","red"),i.css("a::attr(href)").getall())

class makeit(scrapy.Spider):
    name="makeit"
    start_urls=['https://unsplash.com//']
    def parse(self, response):
        logging.getLogger('scrapy').propagate = False
        sel=Selector(response)
        # for i in sel.xpath("//p"):
        # #     print(cs(i.xpath("//p::text()").extract(),"red"))
        # print(sel.xpath("//p").getall())
        
        # print(cs("headings","red"),sel.xpath("//h1").getall())
        print(cs(sel.xpath("//img").getall(),"red"))
        yield{
            'link':sel.xpath("//img/text()").getall()
        }
class javascript_data(scrapy.Spider):
    name="javascript_data"
    start_urls=['https://unsplash.com/']
    def parse(self,response):
        java_data=response.css('script::text').getall()
        print(cs("javascript data","red"),java_data)
        for i in java_data:
            if "window.__INITIAL_STATE__" in i:
                print(cs("javascript data","red"),i)
                print(cs("javascript data","red"),i.split("window.__INITIAL_STATE__ = ")[1].split(";")[0])
                print(cs("javascript data","red"),i.split("window.__INITIAL_STATE__ = ")[1].split(";")[0].replace("'","").replace(" ",""))
                print(cs("javascript data","red"),i.split("window.__INITIAL_STATE__ = ")[1].split(";")[0].replace("'","").replace(" ","").replace("{","").replace("}",""))
                print(cs("javascript data","red"),i.split("window.__INITIAL_STATE__ = ")[1].split(";")[0].replace("'","").replace(" ","").replace("{","").replace("}","").replace("[","").replace("]",""))
                print(cs("javascript data","red"),i.split("window.__INITIAL_STATE__ = ")[1].split(";")[0].replace("'","").replace("",""))
            yield {
            "data":i
        }
        data=chompjs.chompjs(java_data)
        print(cs("data","red"),data)
class gold_price(scrapy.Spider):
    name="gold_price"
    start_urls=['https://www.kitco.com/']
    def parse(self,response):
        logging.getLogger('scrapy').propagate = False
        m = '.item_title_info'
        l='.gpxTickTab_oz_price'
        print("price is ::")
        print(cs("gold price","red"),response.css(l).extract_first())
        