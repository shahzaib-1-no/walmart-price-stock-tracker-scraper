# Walmart Price & Stock Tracker Scraper

🚀 A professional **Walmart Web Scraper** built with **Python, Scrapy, Playwright, PostgreSQL, and Streamlit**.  
This tool helps you monitor **Walmart product prices, stock availability, reviews, and ratings** with automated alerts and a dashboard.  

---

## 🔹 Features
- Scrape **5000+ Walmart products**:
  - Product Title  
  - Price  
  - Stock Status  
  - Reviews & Ratings  
- **Playwright + Scrapy Integration** → handle dynamic pages & avoid bot detection  
- **Proxy rotation + headless scraping** for large-scale data collection  
- **PostgreSQL storage** for structured & historical data  
- **Daily automation** using cron jobs (or Airflow for advanced pipelines)  
- **Email alerts** for price drops & out-of-stock products  
- **Interactive dashboard** with Streamlit to explore data  

---

## 🔹 Tech Stack
- **Language:** Python  
- **Scraping Tools:** Scrapy, Playwright  
- **Database:** PostgreSQL  
- **Automation:** Cron Jobs / Airflow  
- **Dashboard:** Streamlit  
- **Email Alerts:** SMTP / SendGrid  
- **Containerization (Optional):** Docker  

---

## 🔹 Project Workflow
1. **Scrapy + Playwright** → Extract Walmart product details dynamically  
2. **Data Cleaning** → Format raw scraped data  
3. **Database Layer** → Store in PostgreSQL with product_id & timestamps  
4. **Scheduling** → Automate scraping daily via cron/Airflow  
5. **Alerts System** → Send email on price/stock changes  
6. **Streamlit Dashboard** → Visualize products, filter data, see trends  

---

## 🔹 Database Schema (PostgreSQL)
```sql
products (
    product_id VARCHAR PRIMARY KEY,
    title TEXT,
    price NUMERIC,
    stock_status TEXT,
    reviews INT,
    rating FLOAT,
    date TIMESTAMP DEFAULT NOW()
)
