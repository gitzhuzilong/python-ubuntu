# -*- coding: utf-8 -*-
import scrapy

from movie.items import MovieItem

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie/']

    def parse(self, response):
        div_list = response.xpath('//div[contains(@class, "col-xs-1-5")]')
        for odiv in div_list:
            item = MovieItem()
            item['post'] = odiv.xpath('.//img/@data-original').extract_first()
            item['name'] = odiv.xpath('.//img/@alt').extract_first()
            item['score'] = odiv.xpath('.//h1/em/text()').extract_first().strip(' -')
            item['_type'] = odiv.xpath('.//div[@class="otherinfo"]').xpath('string(.)').extract_first()
            detail_url = odiv.xpath('.//h1/a/@href').extract_first()
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        item['director'] = response.xpath('//div[@class="col-xs-8"]/table//tr[1]/td[2]').xpath('string(.)').extract_first()
        item['editor'] = response.xpath('//div[@class="col-xs-8"]/table//tr[2]/td[2]').xpath('string(.)').extract_first()
        item['actor'] = response.xpath('//div[@class="col-xs-8"]/table//tr[3]/td[2]').xpath('string(.)').extract_first().replace(' ', '').replace('显示全部', '')
        item['long_time'] = response.xpath('//div[@class="col-xs-8"]/table//tr[8]/td[2]/text()').extract_first()
        item['introduce'] = response.xpath('//div[@class="col-xs-12 movie-introduce"]').xpath('string(.)').extract_first().replace(' ', '').replace('显示全部', '')
        yield item
        # item['download_url'] = response.xpath('//div[@class="col-xs-8"/table//tr[6]/td[2]').xpath('string(.)').extract_first()