import scrapy
from walmart_tracker.items import WalmartTrackerItem
import glob, os
from scrapy.http import HtmlResponse
from walmart_tracker.itemloaders import WalmartProductLoader
class WalmartProductsParserSpider(scrapy.Spider):
    name = "walmart_products_parser"
    def start_requests(self):
        """
            Read all saved HTML files from the 'products' folder.
            For each file, create an HtmlResponse so Scrapy can parse it like a normal web page.
        """
        files = glob.glob("products/*.html")
        for file in files:
            try:
                abs_path = os.path.abspath(file)
                self.logger.info(f"Reading HTML file: {file}")
                with open(file, 'r', encoding='utf-8') as f:
                    html = f.read()
                    yield  scrapy.Request(
                        url=f"file:///{abs_path}",  # dummy URL for reference
                        callback=self.parse,
                        meta={'html': html, 'file': file}
                    )
            except Exception as e:
                self.logger.error(f"Error While Getting Files: {e}")


    def parse(self, response):
        """
            Parse each product card from the HTML page.
            Extract fields like title, URL, image, brand, price, rating, reviews, badge, and delivery info.
            Yield WalmartTrackerItem for each product.
        """
        try:
            for product in response.xpath('//div[contains(@class,"mb0 ph0-xl pt0-xl")]'):
                url = f"https://www.walmart.com{product.xpath('.//a[@link-identifier]/@href').get()}"
                loader = WalmartProductLoader(item=WalmartTrackerItem(), selector=product)
                loader.add_xpath('title', './/span[@data-automation-id="product-title"]/text()')
                loader.add_xpath('image', './/img[@data-testid="productTileImage"]/@src')
                loader.add_value('url', url)
                loader.add_xpath('brand', './/div[contains(@class,"mb1 mt2")]/text()')
                loader.add_xpath('price', './/div[@data-automation-id="product-price"]//div/text()')
                loader.add_xpath('price_range', './/div[contains(text(),"Options from")]/text()')
                loader.add_xpath('rating', './/span[@data-testid="product-ratings"]/@data-value')
                loader.add_xpath('reviews', './/span[@data-testid="product-reviews"]/@data-value')
                loader.add_xpath('badge', './/span[@data-testid="badgeTagComponent"]//span/text()')
                loader.add_xpath('delivery', './/div[@data-automation-id="fulfillment-badge"]//text()')

                item = loader.load_item()
                yield item
        except Exception as e:
            self.logger.error(f"Error parsing products on {response.url}: {e}")

            
