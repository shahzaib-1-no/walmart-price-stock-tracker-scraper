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

## 🔹 Database Schema (PostgreSQL)
```sql
CREATE TABLE products (
    product_id VARCHAR PRIMARY KEY,
    title TEXT,
    price NUMERIC,
    stock_status TEXT,
    reviews INT,
    rating FLOAT,
    date TIMESTAMP DEFAULT NOW()
);
```

---

## 🔹 Installation

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
scrapy crawl walmart_spider
```
This will scrape Walmart products and insert the data into **PostgreSQL**.

### 2. Export Data (Optional)
```bash
scrapy crawl walmart_spider -o output.json
scrapy crawl walmart_spider -o output.csv
```

### 3. Run Streamlit Dashboard
```bash
streamlit run dashboard.py
```
Open the link in your browser to view the dashboard (default: http://localhost:8501).

### 4. Setup Automation
- Add cron job for daily scraping:
```bash
0 9 * * * /usr/bin/python3 /path/to/project/scrapy crawl walmart_spider
```
(This example runs daily at 9 AM)

---

## 🔹 Example Output
| Product Title | Price | Stock | Reviews | Rating |
|---------------|-------|-------|---------|--------|
| iPhone 14     | $799  | In Stock | 1250 | 4.6 ⭐ |
| Samsung TV    | $599  | Out of Stock | 850 | 4.3 ⭐ |

---

## 🔹 Alerts Example
📧 **Email Notification:**  
- *Product:* iPhone 14  
- *Status:* Out of Stock  
- *Price Change:* $799 → $749  

---

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

