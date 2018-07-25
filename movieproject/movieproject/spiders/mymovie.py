# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider
from scrapy.spider import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from movieproject.items import MovieprojectItem

class MymovieSpider(RedisCrawlSpider):
    name = 'mymovie'
    allowed_domains = ['www.id97.com']
    redis_key = 'mymoviespider:start_urls'
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 400,
        }
    }
    #提取页码链接
    page_link = LinkExtractor(allow=r'/movie/\?page=\d')
    detail_link = LinkExtractor(restrict_xpaths='//div[contains(@class, "col-xs-1-5")]/div/a')
    download_links = LinkExtractor(allow=r'/res/\d\.html')
    rules = (
        #页码只跟进不提取详情
        Rule(page_link, follow=True),
        #详情页无需跟进
        Rule(detail_link, callback='parse_item', follow=False),
        Rule(download_links, callback='')
    )
    def parse_item(self, response):
        item = MovieprojectItem()
        item['name'] = response.xpath('//h1/text()').xpath('string(.)').extract_first()
        item['director'] = response.xpath('//tbody/tr[1]/td[2]/a/text()').extract_first()
        item['writer'] = response.xpath('//tbody/tr[2]/td[2]').xpath('string(.)').extract_first()
        item['actor'] = response.xpath('//tbody/tr[3]/td[2]').xpath('string(.)').extract_first().replace('显示全部', '')
        item['_type'] = response.xpath('//tbody/tr[4]/td[2]').xpath('string(.)').extract_first()
        item['area'] = response.xpath('//tbody/tr[5]/td[2]').xpath('string(.)').extract_first()
        item['language'] = response.xpath('//tbody/tr[6]/td[2]').xpath('string(.)').extract_first()
        item['release_date'] = response.xpath('//tbody/tr[7]/td[2]').xpath('string(.)').extract_first()
        item['duration'] = response.xpath('//tbody/tr[8]/td[2]').xpath('string(.)').extract_first()
        item['grade'] = response.xpath('//tbody/tr[10]/td[2]').xpath('string(.)').extract_first()
        item['introduce'] = response.xpath('//div[@class="col-xs-12 movie-introduce"]/p/text()').extract_first().replace('\u3000', '')
        yield item