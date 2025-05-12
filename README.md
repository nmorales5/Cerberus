# Rent Rank: Single-Family Rentals

## 📦 Tech Stack

- **Languages & Libraries**:  
  - Python  
  - SQL  
  - `sqlalchemy`, `pandas`, `psycopg2-binary`, `python-dotenv`, `requests`, `beautifulsoup4`

- **Tools & Platforms**:  
  - PostgreSQL (AWS RDS)  
  - GitHub Actions  
  - Looker Studio  

---

## 🎯 Project Objective

This project helps institutional real estate investors identify U.S. single-family rental (SFR) markets that offer high rental yield and pricing efficiency. By integrating web-scraped and API data, the analysis ranks housing markets based on return potential, allowing investment professionals to prioritize high-performing asset classes.

---

## 🏢 Job Description

This project is based on the Analyst, Data Science – RMBS role at Cerberus Capital Management. The job involves analyzing housing data, calculating financial metrics, and building tools to support real estate investment strategies. The position requires strong SQL and Python skills, with an emphasis on turning raw data into actionable insights for investment decisions.

> 📄 [View Job Description](./proposal/Job_Description.pdf)

---

## 🗂️ Data

### Sources
- **Zillow API (via RapidAPI)** – Provided listing prices, rent estimates, square footage, and bedrooms.  
- **Craigslist (Web Scraped)** – Captured real-time rental prices, square footage, and location from the Los Angeles housing market.

### Characteristics
- Data was collected via automated scripts, cleaned in Python, and loaded into an AWS-hosted PostgreSQL database.
- Tables were structured for analysis using SQL best practices, including CTEs, joins, aggregate functions, and window functions.

---

## 📓 Notebooks / Python Scripts

- **Zillow_API_Extract_Load_Raw.ipynb**: Extracts and loads Zillow data via API  
- **Craigslist_Web_Scrape_Extract_Load_Raw.ipynb**: Scrapes and loads Craigslist rental listings  
- **Zillow_API_SQL_Analysis.ipynb**: Calculates rental yield and compares prices by bedroom  
- **Craigslist_Web_Scrape_SQL_Analysis.ipynb**: Evaluates rent, size, and cost-efficiency by unit type

---

## 🔮 Future Improvements

- **Collect higher-quality and more granular data**, especially for web-scraped sources.  
  Better data would improve the depth of analysis and the reliability of visualizations.
- Expand analysis to include **multiple markets or time periods** for broader insights.

---

