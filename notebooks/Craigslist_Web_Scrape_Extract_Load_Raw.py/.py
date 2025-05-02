import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy
import os
from dotenv import load_dotenv
import re
import time

# Load environment variables
load_dotenv()

# Step 1: Setup
base_url = "https://losangeles.craigslist.org"
search_url = f"{base_url}/search/apa"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(search_url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

postings = soup.find_all("li", class_="cl-static-search-result")
print(f"🔍 Found {len(postings)} posts. Scraping first 50...")

results = []

for i, post in enumerate(postings[:50]):
    try:
        a_tag = post.find("a", href=True)
        if not a_tag:
            print(f"⚠️ No link found for post {i+1}")
            continue

        post_url = a_tag["href"]
        time.sleep(1)  # Be polite to Craigslist

        post_res = requests.get(post_url, headers=headers)
        post_soup = BeautifulSoup(post_res.content, "html.parser")

        # Price
        price_tag = post_soup.find("span", class_="price")
        price = price_tag.get_text(strip=True).replace("$", "").replace(",", "") if price_tag else None

        # Beds and sqft
        housing_tag = post_soup.find("span", class_="housing")
        beds = sqft = None
        if housing_tag:
            text = housing_tag.get_text()
            bed_match = re.search(r"(\d+)br", text)
            sqft_match = re.search(r"(\d+)\s*ft", text)
            beds = int(bed_match.group(1)) if bed_match else None
            sqft = int(sqft_match.group(1)) if sqft_match else None

        # Address
        map_tag = post_soup.find("div", class_="mapaddress")
        address = map_tag.get_text(strip=True) if map_tag else "Los Angeles, CA"

        results.append({
            "address": address,
            "price_usd": int(price) if price and price.isdigit() else None,
            "beds": beds,
            "sqft": sqft
        })

        print(f"✅ [{i+1}] {address} — ${price}, {beds}br")

    except Exception as e:
        print(f"⚠️ Error on post {i+1}: {e}")

# Step 2: Convert to DataFrame
df = pd.DataFrame(results)

# Step 3: Connect to PostgreSQL
db_user = os.getenv("PG_USER")
db_pass = os.getenv("PG_PASSWORD")
db_host = os.getenv("PG_HOST")
db_port = "5432"
db_name = os.getenv("PG_DB")

connection_str = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
engine = sqlalchemy.create_engine(connection_str)

# Step 4: Load into raw.craigslist_data
if not df.empty:
    df.to_sql("craigslist_data", engine, schema="raw", if_exists="replace", index=False)
    print("✅ Craigslist data loaded to raw.craigslist_data")
else:
    print("⚠️ No data loaded — table created but empty")