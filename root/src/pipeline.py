import pandas as pd
from pathlib import Path
from root.src.data_cleaning import clean_data
from root.src.feature_engineering import feature_engineering
from root.src.validation import validation
import csv

BASE_DIR = Path(__file__).resolve().parent.parent
listings_data_path = BASE_DIR / "data" / "raw" / "listings.csv"
reviews_data_path = BASE_DIR / "data" / "raw" / "reviews.csv"
neighborhoods_data_path = BASE_DIR / "data" / "raw" / "neighbourhoods.csv"

def load_data(input_path):
    """
    Load raw dataset from CSV file.

    Parameters
    path : str or Path

    Returns
    pd.DataFrame
    """
    return pd.read_csv(
            input_path,
            encoding="utf-8",
            quotechar='"',
            escapechar="\\",
            quoting=csv.QUOTE_MINIMAL,
            on_bad_lines="skip",
            low_memory=False
        )

def save_data(df, output_path):
    """
    Save dataset in a CSV file.

    Parameters
    ----------
    path : str or Path

    Returns
    -------
    pd.DataFrame after all transformations
    """
    
    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig",
        sep=";",
        quoting=csv.QUOTE_ALL
    )
    
def run_pipeline(input_path, output_path):
    """
    Load dataset from CSV file.

    Parameters
    ----------
    input path : str or Path
    output path : str or Path

    Returns
    -------
    Output pd.DataFrame after cleaning, engineering and validation
    """
    
    df = load_data(input_path)
    df = clean_data(df)
    df = feature_engineering(df)
    df = validation(df)
    save_data(df, output_path)
    
run_pipeline(BASE_DIR / "data" / "raw" / "listings.csv", BASE_DIR / "data" / "processed" / "listings_data_clean.csv")