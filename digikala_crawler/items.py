import scrapy
class DigikalaCrawlerItem(scrapy.Item):
# define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    # body = scrapy.Field()
    # category = scrapy.Field()
    # tags = scrapy.Field()
    # pubDate = scrapy.Field()
