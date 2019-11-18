# -*- coding: utf-8 -*-
import scrapy
import re
from mySpider.items import MyspiderItem

class ToScrapeSpiderXPath(scrapy.Spider):
    SS = input("请输入要搜索的内容：")
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ["https://www.baidu.com/s?ie=UTF-8&wd={0}".format(SS)]

    def parse(self, response):

        node_list = response.xpath('//*[@id="content_left"]/div')
        # with open('baidu_xpath.text', 'w', encoding='utf-8')as f:
        #   f.writelines(node_list.extract())

        for quote in node_list:
            item = MyspiderItem()

            # 筛选掉广告
            if len(quote.xpath('./h3')) > 0:
                name_baidu_re = quote.xpath('./h3/a').extract_first()
                # print("q"*30, "\n", name_baidu_re)
                try:
                    # 用正则表达式清洗数据，解决em的问题
                    ZZ = '_blank\\"\>.*'
                    name_baidu = re.search(ZZ, name_baidu_re).group().replace("_blank\">", "").replace("<em>", "").replace("</em>", "").replace("</a>","")
                    # print("*" * 30, "\n", name_baidu)
                    link_baidu = quote.xpath('./h3/a/@href').extract_first()

                    item['name_baidu'] = name_baidu
                    item['link_baidu'] = link_baidu
                    yield item
                except:pass