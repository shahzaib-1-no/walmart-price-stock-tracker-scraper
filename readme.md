# Walmart Price & Stock Tracker Scraper

🚀 A **professional Walmart Web Scraper** built with **Python, Scrapy, Playwright, and PostgreSQL**.  
Designed for **real-time price monitoring, stock availability tracking, reviews, and ratings analysis**.  

---

## 🔹 Features
- Scrape **detailed Walmart product data**:
  - Title  
  - Image  
  - URL  
  - Brand  
  - Price + Price Range  
  - Rating  
  - Reviews Count  
  - Badge (Best Seller / Rollback / Clearance etc.)  
  - Delivery Options  

- **Playwright + Scrapy Integration** → handle **JavaScript-heavy & dynamic pages** smoothly  
- **Proxy rotation + headless mode** → scale scraping & bypass bot detection  
- **PostgreSQL storage** → structured, queryable, and historical product data  
- **Scalable architecture** → easy to extend for more attributes or categories  

---

## 🔹 Tech Stack
- **Language:** Python  
- **Scraping Tools:** Scrapy, Playwright  
- **Database:** PostgreSQL  
- **Containerization (Optional):** VENV  

---

## 🔹 Database Schema (PostgreSQL)  
```sql
CREATE TABLE products (
    product_id VARCHAR PRIMARY KEY,
    title TEXT,
    brand TEXT,
    image TEXT,
    url TEXT,
    price NUMERIC,
    price_range TEXT,
    stock_status TEXT,
    reviews INT,
    rating FLOAT,
    badge TEXT,
    delivery TEXT,
    date TIMESTAMP DEFAULT NOW()
);

## 🔹 Installation
```
### 1. Clone Repository
```bash
git clone https://github.com/username/walmart-price-stock-tracker-scraper.git
cd walmart-price-stock-tracker-scraper
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```bash
playwright install
```

### 5. Setup PostgreSQL Database
- Install PostgreSQL (if not installed)  
- Create a database:
```sql
CREATE DATABASE walmart_tracker;
```
- Update `settings.py` or `.env` file with your DB credentials:
```
DB_NAME=walmart_tracker
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## 🔹 Usage

### 1. Run Scraper
```bash
scrapy crawl walmart_products_parser
scrapy crawl walmart_products
```
This will scrape Walmart products and insert the data into **PostgreSQL**.

### 2. Export Data (Optional)
```bash
scrapy crawl walmart_products -o output.csv
```
## 🔹 Use Cases
- 🛒 **E-commerce Monitoring** → Track Walmart product prices  
- 📉 **Price Comparison** → Compare Walmart with competitors  
- 📦 **Stock Tracking** → Alerts when product goes out of stock  
- 📊 **Market Research** → Analyze reviews & ratings  

---

## 🔹 License
This project is licensed under the **MIT License** – completely free for both personal and commercial use.  
See the [LICENSE](LICENSE) file for details.  

---

## 🔹 Author
👨‍💻 Created & maintained by [Shahzaib Ali](https://github.com/shahzaib-1-no)  
📬 For collaboration or freelance work: **sa4715228@gmail.com**  

