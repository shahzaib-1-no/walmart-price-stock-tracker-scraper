import scrapy
import json
from urllib.parse import urlencode 
from urllib.parse import urljoin as py_urljoin
from scrapy_playwright.page import PageMethod
import os

class WalmartProductsSpider(scrapy.Spider):
    name = "walmart_products"
    def start_requests(self):
        self.API_KEY="bdb4bb5d-ecbe-455c-b285-e133b75a9de1"
        url = "https://www.walmart.com/search?q=watch&page=1&affinityOverride=default"
        payload = {"api_key": self.API_KEY, "url": url}
        proxy_url = "http://proxy.scrapeops.io/v1/?" + urlencode(payload)
        yield scrapy.Request(
            url=proxy_url,
            meta={
                "playwright": True,
                "playwright_page_goto_kwargs": {
                    "timeout": 120000,   # 120 sec
                    "wait_until": "domcontentloaded"   # "networkidle" ki jagah
                },
                "playwright_page_methods": [
                    PageMethod("wait_for_timeout", 5000)   # 5 sec wait
                ],
                "page_num": 1,
            },
            callback=self.parse,
            errback=self.handle_error,
            dont_filter=True,
        )
    
    def make_request(self, url,page_num):
        proxy_url= f"http://proxy.scrapeops.io{url}"
        self.logger.info(f"This is Proxy_url: {proxy_url}")
        return scrapy.Request(
            url=proxy_url,
            meta={
                "playwright": True,
                "playwright_page_goto_kwargs": {
                    "timeout": 120000,   # 120 sec
                    "wait_until": "domcontentloaded"   # "networkidle" ki jagah
                },
                "playwright_page_methods": [
                    PageMethod("wait_for_timeout", 5000)   # 5 sec wait
                ],
                "page_num":page_num,
            },
            callback=self.parse,
            errback=self.handle_error,
            dont_filter=True
        )

    def handle_error(self, failure):
        self.logger.error(f"Request failed: {failure.value}")
        # Retry logic (optional)
        request = failure.request
        yield scrapy.Request(
            url=request.url,
            meta=request.meta,
            callback=self.parse,
            errback=self.handle_error,
            dont_filter=True,
            priority=request.priority - 1  # Lower priority retry
        )
   
    def parse(self, response):
        """
            Extract products from Walmart search results.
            Save structured data in HTML file and handle pagination.
        """
        try:
            page_num = response.meta.get("page_num",1)
            # EXTRACT PRODUCTS
            products = response.xpath('//div[contains(@class, "mb0 ph0-xl pt0-xl bb b--near-white w-25")]').getall()
            self.logger.info(f"Page {page_num} Found {len(products)} Products")

            # Save Products
            filename = f"products/product_list_page_{page_num}.html"
            os.makedirs("products", exist_ok=True) 
            
            with open(filename, "w", encoding="utf-8") as f:
                for product in products:
                    f.write(product + "\n\n")
                    
            # --- Pagination ---
            next_page_href = response.xpath('//a[contains(@aria-label,"Next")]/@href').get()
            
            if next_page_href:
                yield self.make_request(next_page_href, page_num + 1)
        except Exception as e:
            self.logger.error(f"Parsing failed on page {response.meta.get('page_num')}: {e}", exc_info=True)
            
