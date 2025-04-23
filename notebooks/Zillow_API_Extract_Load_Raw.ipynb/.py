# Zillow_API_Extract_Load_Raw.ipynb

import requests
import pandas as pd
import sqlalchemy
import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# Step 1: API Setup
# -----------------------------------

API_URL = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
headers = {
    "X-RapidAPI-Key": os.getenv("ZILLOW_API_KEY"),  # <--- REPLACE this with your real key
    "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
}

# Sample location: Los Angeles, CA
params = {
    "location": "Los Angeles, CA"
}

# Make API request
response = requests.get(API_URL, headers=headers, params=params)
data = response.json()

# -----------------------------------
# Step 2: Clean the JSON
# -----------------------------------

# print("Raw API response:", data)
# -----------------------------------
# Step 2: Clean the JSON (safely)
# -----------------------------------

properties = data.get("props", [])

# Check if the response contains any data
if properties:
    df = pd.json_normalize(properties)
    #print("Columns returned:", df.columns.tolist())  # Helpful for debugging

    # Adjust these fields based on what the API returns
# Try these updated fields based on the actual response
    df = df[["address", "price", "bedrooms", "bathrooms", "livingArea", "rentZestimate"]]
    df.columns = ["address", "price", "beds", "baths", "sqft", "rent_estimate"]


    print(df.head())
else:
    print("No properties returned from API.")
    df = pd.DataFrame()  # So the rest of the script doesn't crash


# -----------------------------------
# Step 3: Connect to AWS RDS (PostgreSQL)
# -----------------------------------

# Update with your real DB credentials
db_user = os.getenv("PG_USER")
db_pass = os.getenv("PG_PASSWORD")
db_host = os.getenv("PG_HOST")
db_port = "5432"
db_name = os.getenv("PG_DB")

connection_str = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
engine = sqlalchemy.create_engine(connection_str)

# -----------------------------------
# Step 4: Write to RAW schema
# -----------------------------------

if not df.empty:
    df.to_sql("zillow_data", engine, schema="raw", if_exists="replace", index=False)
    print("Data loaded to cerberus.raw.zillow_data")
else:
    print("No data to write to database.")


