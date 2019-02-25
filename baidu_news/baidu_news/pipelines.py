# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduNewsPipeline(object):
    def __init__(self):
        self.out_file = open("data\\news.txt", "w", encoding="utf-8")
        self.index = 0
    
    def process_item(self, item, spider):
        self.out_file.write(item['doc'] + "\n")
        self.index += 1
        if self.index % 30 == 0:
            self.out_file.flush()
            print("index : " + str(self.index))
        if self.index == 10000000:
            print("end!!!!!!!!!!!!!!!!!!")
            self.out_file.close()
        return item
    
    def __def__(self):
        self.out_file.close()
