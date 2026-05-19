# Lisbon Housing Market - Data Engineering & Analysis
**Author:** Elton Silva

## Overview:
This project creates a data engineering pipeline and analyzes quarterly data from the Lisbon Housing market for the quarter ending in September 2025.

## Tools used:
- Python 3.10
- SQL

## Commands:
To run the data engineering pipeline:
```bash
python -m root.src.pipeline
```

To create the database:
```bash
python root/sql/listings_db.py
```

## File Structure
```text
- root:
    - dashboard
    - data:
        - processed:
            - listings_data_clean.csv
        - raw:
            - calendar.csv.gz
            - listings.csv
            - listings.csv.gz
            - neighbourhoods.csv
            - neighbourhoods.geojson
            - reviews.csv
            - reviews.csv.gz
    - notebooks:
        - Data_exploration.ipynb
    - sql:
        - listings_db.py
        - queries.sql
    - src:
        - __init__.py
        - data_cleaning.py
        - feature_engineering.py
        - pipeline.py
        - validation.py
    - visuals
        - charts
        - dashboard_screenshots
        - sql_outputs
            - availability_profile_by_avg_reviews.csv
            - availability_profile_by_price.csv
            - availability_profile_vs_host_size_category.csv
            - demand_by_neighbourhood.csv
            - host_size_analysis.csv
            - neighbourhood_price_summary.csv
            - review_activity_by_avg_review.csv
            - review_activity_by_neighbourhood.csv
            - review_activity_by_price.csv
            - room_type_by_avg_estimated_bookings.csv
            - room_type_by_avg_minimum_night.csv
            -room_type_by_avg_price.csv
    - __init__.py
    - README.md
    - requirements.txt
lisbon_using.db
```

## Requirements:
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- Path
- logging