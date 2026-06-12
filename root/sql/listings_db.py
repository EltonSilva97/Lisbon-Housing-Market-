import pandas as pd
import sqlite3

# Load cleaned CSV
df = pd.read_csv("root/data/processed/listings_data_clean.csv", sep=";")

# Create database
conn = sqlite3.connect("lisbon_housing.db")

# Add table
df.to_sql(
    "listings_data_clean",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully!")