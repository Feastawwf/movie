# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道： 数据清洗、去重
# 持久化： 写入txt csv   写入数据库

# scrapy 框架将爬取spider模块和处理层分离开，使得程序更容易扩展
# spider yield生成的item会交给pipline处理。如果爬取速度跟处理速度不一致的话，scrapy框架会自动调度。
# spirder yield相当于生产消费模型中的生产者，pipeline相当于消费者。如果爬取解析速度快于pipeline，那么还没来得及处理的item会进入到队列当中（item_chain）。

class MoviePipeline(object):
    def process_item(self, item, spider):
        # 爬虫部分在for循环中yield item,所以process_item 方法会重复执行
        # open(mode='a')追加模式，如果w模式的话会覆盖掉上次写的信息。
        with open('my_meijutt.text' , 'a',encoding='utf-8') as fp:# 模式为a模式，不会被覆盖
            fp.write(str(item['name']) + '\n') # item 的name
        return item




