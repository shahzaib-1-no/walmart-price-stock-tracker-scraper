# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WalmartTrackerItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    price_range = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()
    badge = scrapy.Field()
    delivery = scrapy.Field()
    
