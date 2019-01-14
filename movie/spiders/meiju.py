# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem   # 这是个路径

class MeijuSpider(scrapy.Spider):
    name = 'meiju'    # 爬虫名字 一个项目可能有多个爬虫，并且每个爬虫有优先级、并发等设置
    allowed_domains = ['meijutt.com']  # 为了防止爬虫项目自动爬去到其它网站，设置权限，每一次请求前都会检查请求的网址是否属于这个域名下，是的话才允许请求。 注意：爬起日志爬取网址后响应为None，检查allowed_domain书写是否正确
    start_urls = ['https://www.meijutt.com/new100.html']  # 要爬取的网址

    def parse(self, response):
        # print(response.status_code,response.content,response.text)
        # 非框架写法 dom = lxml.etree.HTML(response.text) ; dom.xpath('')
        # scrpay框架正则写法 Selector(response.text).xpath('').extract()

        movie_list = response.xpath('/html/body/div[3]/div[3]/div[1]/ul/li')
        for movie_li in movie_list:

            # 解析后跟.extract() 下标[0]   .extract   =  .extract_first()  二者选其一
            # xpath().返回[Selector(),Selector()]     xpath().extract()返回['剧集名','剧集名2'xpath]          xpath().extract_first()  返回'剧集名1'
            # . 表示在子标签基础上继续解析
            name = movie_li.xpath('./h5/a/@title()').extract()[0]
            item = MovieItem()
            # item.name = name  第二种方式
            item['name'] = name

            yield item         # 相当于return