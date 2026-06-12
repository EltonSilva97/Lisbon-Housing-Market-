# Lisbon Housing Market - Data Engineering & Analysis
**Author:** Elton Silva

## Overview

This project performs an end-to-end analysis of the Lisbon housing market using Python, SQL, and Power BI.
The analysis uses a 2025 snapshot of the Lisbon housing market dataset.
The objective is to understand housing dynamics across Lisbon municipalities by analyzing:

- pricing differences
- estimated demand
- host characteristics
- availability patterns
- review activity

## Project Objectives

This project demonstrates:

- Data cleaning and preprocessing
- Data validation practices
- Feature engineering
- Relational database creation
- SQL business analysis
- Dashboard development
- End-to-end data workflows

## Interactive Dashboard

🔗 **Live Dashboard:** [View Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZmU0MDY1ZWYtYWZkMy00M2U4LTg0MmUtMDlhN2Q2ZWZhNGMyIiwidCI6ImU0YmQ2OWZmLWU2ZjctNGMyZS1iMjQ3LTQxYjU0YmEyNDkwZSIsImMiOjh9)

## Key Insights

- Lisbon city had the highest listing volume with over 17,000 listings.
- Cascais showed premium pricing relative to surrounding municipalities.
- Professional hosts tend to charge higher average prices.
- Listings with lower availability generally exhibit stronger review activity, suggesting higher occupancy.

## Business Questions Answered

- Which municipalities generate the highest-value listings?
- What property characteristics have the strongest relationship with price?
- How concentrated is the market among professional hosts?
- Which availability patterns indicate stronger booking demand?
- How does review activity vary across different market segments?
- Which host categories contribute most to the Lisbon housing supply?

## Technology Stack

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Power BI

## Skills Demonstrated

- Data Cleaning
- Data Validation
- Feature Engineering
- ETL Pipelines
- SQL Analytics
- Relational Databases
- Data Visualization
- Dashboard Development
- Business Insight Generation

## Architecture
```text
Raw Airbnb Data
        │
        ▼
Python Cleaning Pipeline
        │
        ▼
Validation Layer
        │
        ▼
Feature Engineering
        │
        ▼
SQLite Database
        │
        ▼
SQL Analysis
        │
        ▼
Power BI Dashboard
```

## Data Quality & Validation

### Missing Value Analysis

Review-related fields contained missing values.
Investigation confirmed these corresponded to listings with zero reviews rather than data collection errors.

These null values were preserved because they represent meaningful business information.

### Data Integrity Checks

- Verified consistency between review columns.
- Checked duplicates.
- Validated data types.
- Confirmed feature engineering outputs.

### Price Standardization

- Currency symbols removed
- Numerical conversion applied
- Format inconsistencies corrected

### Feature Engineering Validation
Created:
- Availability Ratio
- Estimated Bookings per Month
- Minimum Nights 
- Price Category
- Host Size
- Availability Profile
- Review Activity

Derived features were tested to ensure:

- Logical category assignment
- Consistent availability segmentation
- Correct host-size classification


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
    - dashboard:
        - listings_dashboard.pbix
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
        - .gitignore
        - data_cleaning.py
        - feature_engineering.py
        - pipeline.py
        - validation.py
    - visuals:
        - dashboard_screenshots:
            - Executive Overview.png
            - Availability Analysis.png
            - Pricing Analysis.png
            - Reviews Analysis.png
        - sql_outputs
    - __init__.py
    - README.md
    - requirements.txt
- lisbon_housing.db
```

## Dashboard Preview

### Executive Overview
![Executive Overview](./root/visuals/dashboard_screenshots/Executive_Overview.png)

### Availability Analysis
![Availability Analysis](./root/visuals/dashboard_screenshots/Availability_Analysis.png)

### Pricing Analysis
![Pricing Analysis](./root/visuals/dashboard_screenshots/Pricing_Analysis.png)

### Reviews Analysis
![Reviews Analysis](./root/visuals/dashboard_screenshots/Reviews_Analysis.png)

## SQL Analysis

Example business queries:

### Neighbourhood Price Summary
| Municipality | Listing Count | Avg Price (€) |
|-------------|-------------:|--------------:|
| Azambuja | 18 | 871.73 |
| Alenquer | 116 | 504.59 |
| Lourinhã | 573 | 331.34 |
| Cascais | 2,437 | 277.14 |
| Lisboa | 17,428 | 260.31 |
| Sintra | 1,680 | 228.11 |
| Mafra | 1,335 | 171.11 |
| Torres Vedras | 406 | 166.28 |
| Cadaval | 75 | 159.63 |
| Sobral de Monte Agraço | 27 | 141.90 |
| Oeiras | 524 | 121.19 |
| Vila Franca de Xira | 78 | 121.05 |
| Arruda dos Vinhos | 12 | 116.64 |
| Loures | 305 | 107.34 |
| Odivelas | 165 | 99.45 |
| Amadora | 270 | 75.87 |

Premium coastal municipalities such as Cascais command substantially higher prices than most surrounding municipalities, while Lisbon combines high prices with the largest inventory volume.

### Availability Profile by Price
| Availability Profile | Listing Count | Avg Reviews | Avg Reviews / Month |
|---------------------|-------------:|------------:|--------------------:|
| Highly Available | 4,170 | 88.02 | 1.56 |
| Moderately Available | 2,904 | 76.34 | 1.47 |
| Always Available | 11,956 | 75.39 | 1.51 |
| Rarely Available | 6,419 | 42.57 | 0.94 |

Rarely available listings exhibit lower review activity than more available listings, suggesting listing availability is influenced by factors beyond booking volume alone.

### Room Type Analysis
| Room Type | Listing Count | Avg Price (€) |
|-----------|-------------:|--------------:|
| Hotel room | 209 | 9,464.58 |
| Entire home/apt | 18,824 | 216.25 |
| Private room | 6,268 | 113.02 |
| Shared room | 148 | 40.48 |

Entire homes/apartments dominate the Lisbon short-term rental market, while the relatively small hotel-room segment exhibits significantly higher average prices, reflecting its concentration in premium accommodation offerings.