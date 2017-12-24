# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'market_spider'
    start_urls = [
        'https://www.avito.ru/severnaya_osetiya/telefony/iphone?s=101/',
    ]

    def parse(self, response):
        for i in response.xpath('//div[@class="catalog-main catalog_table"]//div[@class="description item_table-description"]'):
            yield {
                'name': i.xpath('.//a[@class="item-description-title-link"]/text()').extract_first(),
                'price' : i.xpath('.//div[@class="about"]/text()').extract_first(),
                'city' : i.xpath('.//div[@class="data"]//p/text()').extract_first(),
            }
        next_page = response.xpath('//a[@class="pagination-page js-pagination-next"]/@href').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))



