from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst
import re
def clean_text(value):
    if value:
        return value.strip().replace('\n','').replace('\r','')
    return ''

def parse_price(value):
    if value:
        try:
            return float(re.sub(r'[^\d.]','', value))
        except:
            return 0
    return 0

class WalmartProductLoader(ItemLoader):
    default_output_processor = TakeFirst()  # automatically pick first element

    # Field-specific processors
    title_in = MapCompose(clean_text)
    brand_in = MapCompose(clean_text)
    price_in = MapCompose(clean_text, parse_price)
    price_range_in = MapCompose(clean_text)
    badge_in = MapCompose(clean_text)
    delivery_in = MapCompose(clean_text)