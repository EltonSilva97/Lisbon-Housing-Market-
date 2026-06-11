import logging

def validation(df):
    """
    Load dataset from CSV file.

    Parameters
    ----------
    path : str or Path

    Returns
    -------
    pd.DataFrame after all verifications
    """
    # Expected: 0
    logging.info(f"{(df['has_reviews'] != (df['number_of_reviews'] > 0)).sum()}")
    
    # Check if there are rows with reviews but reviews_per_month missing
    # Expected: 0 rows
    invalid_reviews_missing = df[
        df['reviews_per_month'].isna() &
        (df['number_of_reviews'] != 0)
    ]
        
    logging.info("Invalid Reviews Missing: %s", len(invalid_reviews_missing))
    
    # Check if there are rows without reviews but with a last_review date
    # Expected: Empty Dataframe
    rows_without_reviews_but_last_review = df[
        (df["number_of_reviews"] == 0) &
        (df["last_review"].notna())
    ]

    logging.info("Rows without reviews but with a last_review date: %s", len(rows_without_reviews_but_last_review))
    
    # Verify if all columns that have NA in both last_review and reviews_per_month have 0 reviews. Logically if a house does not have reviews it cannot have a last date for a review and reviews per month would be 0.
    rows_no_review_missing_dates = df[
        (df["last_review"].isna()) &
        (df["reviews_per_month"].isna()) &
        (df["number_of_reviews"] == 0)
    ]

    logging.info("Rows with no reviews and missing last_review/reviews_per_month: %s", len(rows_no_review_missing_dates))
    
    assert (
        df.loc[df['number_of_reviews'] == 0,
            'reviews_per_month']
        .isna()
        .sum() == 0
    )
    
    assert (
        invalid_reviews_missing.empty
    ), "Rows exist with reviews but missing reviews_per_month"
    
    assert (
        rows_without_reviews_but_last_review.empty
    ), "Rows found without reviews but with last_review"
    
    assert (
        df.loc[
            (df["last_review"].isna()) &
            (df["number_of_reviews"] > 0)
        ].empty
    ), "Rows with reviews but missing last_review"
    
    valid_availability_profiles = {
        "Rarely Available",
        "Moderately Available",
        "Highly Available",
        "Always Available"
    }

    invalid_availability_profiles = df[
        ~df["availability_profile"].isin(valid_availability_profiles)
    ]

    logging.info(
        "Invalid availability_profile rows: %s",
        len(invalid_availability_profiles)
    )

    assert invalid_availability_profiles.empty, (
        "Invalid availability_profile values found"
    )
    
    return df