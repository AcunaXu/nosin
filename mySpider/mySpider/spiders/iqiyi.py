# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class IqiyiSpider(scrapy.Spider):
    name = 'iqiyi'
    allowed_domains = ['list.iqiyi.com']
    start_urls = ['https://list.iqiyi.com/www/4/-------------4-1-1-iqiyi--.html']
    x = 2

    def parse(self, response):

        node_list = response.xpath("//ul[@class='qy-mod-ul']/li")

        for node in node_list:
            item = MyspiderItem()

            name_iqiyi = node.xpath("./div/div/a/@title").extract()
            link_iqiyi = node.xpath("./div/div/a/@href").extract()
            item['name_iqiyi'] = name_iqiyi[0]
            item['link_iqiyi'] = link_iqiyi[0]

            yield item

            # 下一页的地址
        while self.x < 20:
            urls_link = "https://list.iqiyi.com/www/4/-------------4-{0}-1-iqiyi--.html".format(self.x)
            urls = urls_link
            # print("*" * 30 + "没完" + "*" * 30)
            # print(urls)
            yield scrapy.Request(urls, callback=self.parse, dont_filter=True)
            self.x += 1


