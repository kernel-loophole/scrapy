# scrapy
Web Scraping and crawling with scrapy
# scraping wikipedia title pages


![deom_scraping_gif](https://user-images.githubusercontent.com/76658396/168424063-6069a8e9-5638-4bd2-9913-a1a2c63df714.gif)


# simple news scarpper

```python

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
```

