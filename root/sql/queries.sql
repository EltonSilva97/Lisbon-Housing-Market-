-- 1. Average price by neighbourhood group
SELECT
    neighbourhood_group,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price
FROM listings_data_clean
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;


-- 2. Average price by room type
SELECT
    room_type,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price
FROM listings_data_clean
GROUP BY room_type
ORDER BY avg_price DESC;


-- 3. Host size by neighbourhood
SELECT
    neighbourhood_group,
    host_size_category,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price
FROM listings_data_clean
GROUP BY neighbourhood_group, host_size_category
ORDER BY neighbourhood_group, avg_price DESC;


-- 4. Price category by availability profile
SELECT
    availability_profile,
    price_category,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price
FROM listings_data_clean
GROUP BY availability_profile, price_category
ORDER BY availability_profile, avg_price DESC;

-- 5. Review activity by price category
SELECT 
    review_activity, 
    price_category,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(estimated_bookings_month), 2) AS avg_estimated_bookings
FROM listings_data_clean
GROUP BY review_activity, price_category
ORDER BY 
CASE review_activity
    WHEN 'No Reviews' THEN 1
    WHEN 'Low' THEN 2
    WHEN 'Medium' THEN 3
    WHEN 'High' THEN 4
END,
avg_price DESC;

6. -- Which neighbourhoods have the highest estimated demand?
SELECT
    neighbourhood_group,
    COUNT(*) AS listing_count,
    ROUND(AVG(estimated_bookings_month), 2) AS avg_estimated_bookings_month,
    ROUND(AVG(reviews_per_month), 2) AS avg_reviews_per_month
FROM listings_data_clean
GROUP BY neighbourhood_group
ORDER BY avg_estimated_bookings_month DESC;