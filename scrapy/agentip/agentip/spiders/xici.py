# -*- coding: utf-8 -*-
import scrapy


class XiciSpider(scrapy.Spider):
    name = 'xici'
    # allowed_domains = ['xicidaili.com']
    # start_urls = ['http://xicidaili.com/']

    def start_requests(self):
        for i in range(3):
            url='http://quotes.toscrape.com/page/'+str(i+1)
            yield scrapy.Request(url=url,callback=self.parse,method='GET')

    def parse(self, response):
        f=open('C:/Users/kali/Desktop/xici.txt','a+')
        texts=response.xpath('/html/body/div/div[2]/div[1]/div/div/a/text()').getall()

        for   text in  texts:
            f.write(text+'\n\r')
        f.close()
        pass

