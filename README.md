# Rent Rank: Single-Family Rentals

## 🧰 Tech Stack

### Languages & Libraries
- Python
- SQL

### Python Packages
- `pandas`
- `sqlalchemy`
- `psycopg2-binary`
- `requests`
- `beautifulsoup4`
- `python-dotenv`

### Platforms & Tools
- AWS RDS (PostgreSQL)
- GitHub Actions
- Looker Studio

---

## 🎯 Project Objective

### Who am I helping?
Institutional real estate investors evaluating single-family rental (SFR) markets.

### What problem am I solving?
These investors must identify markets with strong rental yield and pricing efficiency—but data is fragmented, inconsistent, or inaccessible in raw form.

### How will I solve their problem?
This project integrates Zillow API data and Craigslist web-scraped data, stores them in a PostgreSQL database, and uses SQL to identify top-performing rental segments. Insights are visualized using Looker Studio.

---

## 🏢 Job Description

This project is based on the **Analyst, Data Science – RMBS** role at **Cerberus Capital Management**, a leading global investment firm. The job focuses on analyzing housing and mortgage-related datasets to support real estate and securitized investment strategies. Core skills include SQL, Python, and the ability to extract insights from complex housing data.

This project directly mirrors the job’s responsibilities by collecting housing data from multiple sources, using SQL to extract insights, and creating actionable dashboards to guide investment strategy.

> 📄 [View Job Description](./proposal/Job_Description.pdf)

---

## 📊 Data

### Sources
- 🔗 **[Zillow API](https://www.zillow.com/homes/12447_rid/)** – Provided listing prices, rent estimates, square footage, and bedrooms.  
- 🔗 **[Craigslist LA Rentals](https://losangeles.craigslist.org/search/apa#search=2~gallery~0)** – Web scraped rental listings with price, size, and bedroom count.

### Characteristics
- Both datasets were cleaned and normalized using `pandas`, then stored in a PostgreSQL database hosted on AWS RDS (`raw` schema).
- Craigslist data reflects real-time rental affordability, while Zillow data reflects listing price trends and rent estimates.
- Queries use CTEs, joins, window functions, and aggregates to derive insights like rental yield and rent per square foot.

---

## 📓 Notebooks / Python Scripts

All files are located in the `/notebooks/` directory.

| File | Purpose |
|------|---------|
| 🔄 [Craigslist_Web_Scrape_Extract_Load_Raw.py](./notebooks/Craigslist_Web_Scrape_Extract_Load_Raw.py) | Scrapes rental listings from Craigslist, extracts price, sqft, and beds, and loads into PostgreSQL |
| 📊 [Craigslist_Web_Scrape_SQL_Analysis.ipynb](./notebooks/Craigslist_Web_Scrape_SQL_Analysis.ipynb) | Analyzes rental value, rent per sqft, and listing trends by bedroom count |
| 🔄 [Zillow_API_Extract_Load_Raw.py](./notebooks/Zillow_API_Extract_Load_Raw.py) | Calls the Zillow API, extracts price and rent estimates, and loads cleaned data into PostgreSQL |
| 📊 [Zillow_API_SQL_Analysis.ipynb](./notebooks/Zillow_API_SQL_Analysis.ipynb) | Calculates rental yield and efficiency using SQL with CTEs and window functions |

---

## 🚀 Future Improvements

1. **Enhance data quality and quantity**: A more complete and reliable dataset—especially from Craigslist—would improve analysis accuracy and visualization impact.
2. **Expand geographic scope**: Including multiple cities or time periods would make the analysis more actionable for institutional investors with regional diversification goals.

---
