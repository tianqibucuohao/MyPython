# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    #allowed_domains = ['www.baidu.com']
    #start_urls = ['https://www.163.com/']
    
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
          #  'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        self.log("===== XPath =====")
        self.log(response.xpath('//title/text()').get())
        self.log("===== XPath End=====")
        self.log("===== CSS =====")
        css=response.css("span.text::text").extract()
        self.log(css)
        self.log("===== CSS End=====")
        filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        self.log('Saved file %s' % filename)
