# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from project.items import ProjectItem


class CbPdfSpider(CrawlSpider):
    name = 'CB-PDF'
    allowed_domains = ['central-bank.org.tt']
    start_urls = ['http://central-bank.org.tt/publications/latest-reports']

    rules = (
        Rule(LinkExtractor(restrict_css='article>div>div>p a'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = 0
        for quote in response.css('article'):
            if i == 0:
                item = ProjectItem()
                file_url = quote.css('a[data-entity-type="file"]::attr(href)').get()
                file_url = response.urljoin(file_url)
                item['file_urls'] = [file_url]
                item['file_names'] = file_url.split("/")[-1]
                i += 1

            yield item
