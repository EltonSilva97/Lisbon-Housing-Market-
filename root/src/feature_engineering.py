import numpy as np
import pandas as pd

def feature_engineering(df):
    """
    Adds informative features
    """
    
    # Fill reviews_per_month with 0 based on the fact that these NAs are based on number_of_reviews being 0. has_reviews column was created to distinguish houses with reviews and houses without.
    df['has_reviews'] = df['number_of_reviews'] > 0
    # Ratio of availability year round
    df['availability_ratio'] = df['availability_365'] / 365
    # Minimum price for reservation
    df['minimum_price'] = df['minimum_nights'] * df['price']
    # Percentage of reviews made in the last year 
    df['pct_review_last_year'] = np.where(
        df['number_of_reviews'] > 0,
        df['number_of_reviews_ltm'] /
        df['number_of_reviews'],
        0
    )
    # Establish a occupancy proxy for monthly bookings
    df['estimated_bookings_month'] = (
        df['reviews_per_month'] / 0.5
    )
    # Group host listings by profile
    df['host_size_category'] = pd.cut(
        df['calculated_host_listings_count'],
        bins=[0, 1, 5, 20, float('inf')],
        labels=[
            'Single Host',
            'Small Host',
            'Professional Host',
            'Commercial Host'
        ]
    )
    # Categorize minimum stay by length
    df['minimum_nights_category'] = pd.cut(
        df['minimum_nights'],
        bins=[0, 2, 7, 30, float('inf')],
        labels=['Short Stay', 'Weekly', 'Monthly', 'Long-term']
    )
    # Set profiles for listings based on price
    df['price_category'] = pd.cut(
        df['price'],
        bins=[0, 50, 100, 200, 500, float('inf')],
        labels=['Budget', 'Affordable', 'Mid-range', 'Premium', 'Luxury']
    )
    # Profile review activity
    df['review_activity'] = pd.cut(
        df['reviews_per_month'],
        bins=[-1, 0, 1, 5, float('inf')],
        labels=['No Reviews', 'Low', 'Medium', 'High']
    )       
    # Profile listings by availability ratio
    df['availability_profile'] = pd.cut(
        df['availability_ratio'],
        bins=[0, 0.25, 0.5, 0.75, 1],
        labels=[
            'Rarely Available',
            'Moderately Available',
            'Highly Available',
            'Always Available'
        ],
        include_lowest=True
    )
    return df