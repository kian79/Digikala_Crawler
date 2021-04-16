import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from digikala_crawler.items import DigikalaCrawlerItem

class DigikalaSpider(CrawlSpider):
    name = 'Digikala'
    allowed_domains = ['www.digikala.com']
    start_urls = ['https://www.digikala.com']

    rules = [Rule(LinkExtractor(allow=r'/product/dkp-\d+/[^/]+$',), callback='parse_kala', follow=False),
             Rule(LinkExtractor(allow=(r'main/[^/]',)), follow=True),
             Rule(LinkExtractor(allow=(r'search/[^/]'   ,)), follow=True)]

    def parse_kala(self, response):
        self.logger.info(f"\n parse_kala called\n{response.request.url}\n")
        item = DigikalaCrawlerItem()
        item['title'] = response.xpath('//h1[@class="c-product__title"]/text()').get().strip()
        item['category'] = response.xpath('//ul[@class="c-breadcrumb"]/li//text()').getall()
        item['price'] = response.xpath('//div[@class="c-product__seller-price-real"]//text  ()').get()
        self.logger.info(f"title : {item['title']}")
        self.logger.info(f"category : {item['category']}")
        self.logger.info(f"price : {item['price']}")

        yield item
