import logging
import pandas as pd

def correct_datatypes(df):
    """
    Correct column data types.

    Converts:
    - last_review -> datetime
    - host_id -> string
    """
    
    # Correct last_review data type to datetime and host_id to string
    df["last_review"] = pd.to_datetime(df["last_review"], errors='coerce')
    df["host_id"] = df["host_id"].map(str)
    return df
    
def handle_missing_values(df):
    """
    Treats missing values
    
    Treatment:
    - Adds flags for every column with missing values
    - For every reviews_per_month that is missing and has 0 reviews, it is set to zero
    - Checks before and after by logging columns with more than 10% missing values
    """
        
    # Columns with >10% missing were evaluated for imputation strategies.
    missing_summary = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_pct": (df.isna().mean() * 100).round(2)
    }).sort_values("missing_pct", ascending=False)

    logging.info("\n%s", missing_summary[missing_summary["missing_count"] > 0])
        
    # Add flags for columns with missing values
    for col in ['price', 'host_name', 'license', 'last_review', 'reviews_per_month']:
        df[f'{col}_missing'] = df[col].isna() 

    mask = (df['number_of_reviews'] == 0) & df['reviews_per_month'].isna()
    df.loc[mask, 'reviews_per_month'] = 0

    # Check if reviews_per_month is not missing values anymore
    # Expected: 0
    logging.info("Reviews per month nulls: %s", df['reviews_per_month'].isna().sum())
        
    missing_summary_post_cleaning = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_pct": (df.isna().mean() * 100).round(2)}
    ).sort_values("missing_pct", ascending=False)

    logging.info("Null values summary post cleaning: %s", missing_summary_post_cleaning)
    
    return df


def clean_data(df):
    """
    Applies the previous steps to the dataset

    Returns
    -------
    pd.DataFrame after all data cleaning steps
    """
    
    df = df.copy()
    df = correct_datatypes(df)
    df = handle_missing_values(df)
    
    return df
    