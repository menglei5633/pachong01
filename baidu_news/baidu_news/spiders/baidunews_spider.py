# -*- coding: utf-8 -*-
import scrapy
from baidu_news.items import BaiduNewsItem


class BaidunewsSpiderSpider(scrapy.Spider):
    name = 'baidunews_spider'
    allowed_domains = ['news.baidu.com', 'baijiahao.baidu.com', 'mbd.baidu.com']
    start_urls = ['https://news.baidu.com']

    def parse(self, response):
        p_list = response.xpath("//div[@class='article-content']/p")
        title = response.xpath("//div[@class='article-title']/h2/text()").extract_first()
        if p_list and title:
            str_ = title.split("\n")[0] + " "
            for p in p_list:
                p_str = p.xpath("string(./span)").extract_first()
                p_str = p_str.strip()
                str_ += p_str + " "
#            print(str_)
            news = BaiduNewsItem()
            news['doc'] = str_
            yield news
        
        menu_list = response.xpath("//div[@id='channel-all']/div/ul/li/a/@href").extract()
        if menu_list:
#            print("aaa : "+str(len(menu_list)))
            for menu in menu_list:
#                print(menu)
                yield scrapy.Request("https://news.baidu.com" + menu, callback=self.parse)
                
        doc_list = response.xpath("//ul[contains(@class,'focuslistnews')]/li/a/@href").extract()
        if doc_list:
#            print("bbb : "+str(len(doc_list)))
            for doc in doc_list:
#                print(doc)
                yield scrapy.Request(doc, callback=self.parse)
                
#        作者最近文章
        doc_list1 = response.xpath("//div[@class='recent-article']/h2/ul/li/h3/a/@href").extract()
        if doc_list1:
#            print("bbb : "+str(len(doc_list)))
            for doc in doc_list1:
#                print(doc)
                yield scrapy.Request(doc, callback=self.parse)
                
#       相关文章
        doc_list2 = response.xpath("//div[@class='related-news']/div/ul/li//div[1]/div[2]/div[1]/h3/a/@href").extract()
        if doc_list2:
#            print("bbb : "+str(len(doc_list)))
            for doc in doc_list2:
#                print(doc)
                yield scrapy.Request(doc, callback=self.parse)
#        //div[@class='menu-list']/ul/li/a/@href
#        //*[@id="channel-all"]/div/ul/li[1]/a
        
        
        
        
