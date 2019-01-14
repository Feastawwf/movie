# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'    # 爬虫名字 一个项目可能有多个爬虫，并且每个爬虫有优先级、并发等设置
    allowed_domains = ['meijutt.com']  # 为了防止爬虫项目自动爬去到其它网站，设置权限，每一次请求前都会检查请求的网址是否属于这个域名下，是的话才允许请求。 注意：爬起日志爬取网址后响应为None，检查allowed_domain书写是否正确
    start_urls = ['https://www.meijutt.com/new100.html']  # 要爬取的网址

    def parse(self, response):
        movies = response.xpath('/html/body/div[3]/div[3]/div[1]/ul/li')
        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title()').extract()[0]
            yield item