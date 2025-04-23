import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Step 1: Send request to Craigslist
url = "https://losangeles.craigslist.org/search/apa"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Step 2: Extract JSON from <script> tag
script_tag = soup.find("script", id="ld_searchpage_results", type="application/ld+json")

# Step 3: Parse and build DataFrame
if script_tag:
    json_data = json.loads(script_tag.string)
    items = json_data.get("itemListElement", [])

    data = []
    for item in items:
        prop = item.get("item", {})
        data.append({
            "name": prop.get("name", "N/A"),
            "address": prop.get("address", {}).get("addressLocality", "N/A"),
            "region": prop.get("address", {}).get("addressRegion", "N/A"),
            "lat": prop.get("latitude", None)
        })

    df = pd.DataFrame(data)
    print(df.head())
else:
    print("Could not find JSON data.")

import sqlalchemy
import os
from dotenv import load_dotenv

load_dotenv()

# DB connection info from .env
db_user = os.getenv("PG_USER")
db_pass = os.getenv("PG_PASSWORD")
db_host = os.getenv("PG_HOST")
db_port = "5432"
db_name = os.getenv("PG_DB")

# Create engine
connection_str = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
engine = sqlalchemy.create_engine(connection_str)

# Load to cerberus.raw.craigslist_data
if not df.empty:
    df.to_sql("craigslist_data", engine, schema="raw", if_exists="replace", index=False)
    print("Data loaded to cerberus.raw.craigslist_data")
else:
    print("No data to load.")

