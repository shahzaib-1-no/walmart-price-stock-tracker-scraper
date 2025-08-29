import scrapy


class WalmartProductsSpider(scrapy.Spider):
    name = "walmart_products"
    allowed_domains = ["walmart.com"]
    start_urls = ["https://walmart.com"]

    def parse(self, response):
        pass
