from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

settings.set('FEED_FORMAT', 'csv')
settings.set('FEED_URI', 'test2.csv')

process = CrawlerProcess(settings)
process.crawl('CB-PDF')
process.start()
