# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2, logging

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WalmartTrackerPipeline:
    def process_item(self, item, spider):
        return item
    
class PostgresPipeline:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='postgres',
                dbname='walmart_tracker',
                port=5432,
            )
            self.cur = self.connection.cursor()
            self.logger.info("PostgreSQL connected successfully")
        except Exception as e:
            self.logger.error(f"Database connection failed: {e}")
        
    def create_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    image TEXT,
                    url TEXT UNIQUE,  -- URL unique banaya
                    brand VARCHAR(100),
                    price FLOAT,
                    price_range VARCHAR(100),
                    rating FLOAT,
                    reviews INT
                )
            """)
            self.connection.commit()
            self.logger.info("Table created (if not exists)")
        except Exception as e:
            self.logger.error(f"Table creation failed: {e}")
            
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        count=0
        try:
            self.cur.execute("""
                INSERT INTO products (title, image, url, brand, price, price_range, rating, reviews)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO UPDATE SET
                    title = EXCLUDED.title,
                    image = EXCLUDED.image,
                    brand = EXCLUDED.brand,
                    price = EXCLUDED.price,
                    price_range = EXCLUDED.price_range,
                    rating = EXCLUDED.rating,
                    reviews = EXCLUDED.reviews
            """, (
                item.get("title"),
                item.get("image"),
                item.get("url"),
                item.get("brand")if item.get("brand") else None,
                float(item.get("price")) if item.get("price") else None,
                item.get("price_range") if item.get("price_range") else None,
                float(item.get("rating")) if item.get("rating") else None,
                int(item.get("reviews")) if item.get("reviews") else None,
            ))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback() 
            self.logger.error(f"Insert/Update failed: {e} | Item: {item}")
        
            
    def close_spider(self, spider):
        try:
            self.cur.close()
            self.connection.close()
            self.logger.info("PostgreSQL connection closed")
        except Exception as e:
            self.logger.error(f"Error closing connection: {e}")

       