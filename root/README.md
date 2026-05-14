# Lisbon Housing Market - Data Engineering & Analysis
**Author:** Elton Silva

## Overview:
This project creates a data engineering pipeline and analyzes quarterly data from the Lisbon Housing market for the quarter ending in September 2025.

## Tools used:
- Python 3.12
- SQL

## Commands:
```bash
python -m root.src.pipeline
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
        - queries.sql
    - src:
        - __init__.py
        - data_cleaning.py
        - feature_engineering.py
        - pipeline.py
        - validation.py
    - visuals
    - __init__.py
    - README.md
    - requirements.txt
```

## Requirements:
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- Path
- logging