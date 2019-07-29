# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:57:05 2019

@author: Administrator
"""

import scrapy

class Quote(scrapy.Spider):
    name = "quote"
    def start_req(self):
        urls=[
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        print('start req')
    
    def parse(self, resp):
        page = resp.url.split("/")[-2]
        filename = 'quote-%s.html' % page
        with open(filename,'wb') as f :
            f.write(resp.body())
        self.log('save file %s'% filename)
        print ('suc')

#def main():
#    q=Quote()
#    q.start_req()
#    print("hello")
#    
#if (__name__=="__main__"):
#    main()