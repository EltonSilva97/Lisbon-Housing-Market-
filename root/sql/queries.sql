-- Neighbourhood exploration
-- 1. Which neighbourhoods are more and least expensive?
SELECT
    neighbourhood_group,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price
FROM listings_data_clean
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;

-- 2. Does neighbourhoods differ in host size?
SELECT
    neighbourhood_group,
    host_size_category,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price
FROM listings_data_clean
GROUP BY neighbourhood_group, host_size_category
ORDER BY neighbourhood_group, avg_price DESC;

-- 3. Which neighbourhoods have the highest estimated demand?
SELECT
    neighbourhood_group,
    COUNT(*) AS listing_count,
    ROUND(AVG(estimated_bookings_month), 2) AS avg_estimated_bookings_month,
    ROUND(AVG(reviews_per_month), 2) AS avg_reviews_per_month
FROM listings_data_clean
GROUP BY neighbourhood_group
ORDER BY avg_estimated_bookings_month DESC;

-- Availability exploration
-- 1. How do availability profiles differ in price?
SELECT
    availability_profile,
    price_category,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price
FROM listings_data_clean
GROUP BY availability_profile, price_category
ORDER BY availability_profile, avg_price DESC;

-- 2. Do more available listings get more reviews?
SELECT
    availability_profile,
    COUNT(*) AS listing_count,
    ROUND(AVG(number_of_reviews), 2) AS avg_reviews,
    ROUND(AVG(reviews_per_month), 2) AS avg_reviews_per_month
FROM listings_data_clean
GROUP BY availability_profile
ORDER BY avg_reviews DESC;

-- 3. Which types of host size categories are more available?
SELECT
    availability_profile,
    host_size_category,
    COUNT(*) AS listing_count,
    ROUND(AVG(availability_ratio), 2) AS avg_availability_ratio,
    ROUND(AVG(calculated_host_listings_count), 2) AS avg_host_size
FROM listings_data_clean
GROUP BY availability_profile, host_size_category
ORDER BY avg_availability_ratio  DESC;

-- Review exploration
-- 1. How does review activity differ by price category?
SELECT 
    review_activity, 
    price_category,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(estimated_bookings_month), 2) AS avg_estimated_bookings_month
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

-- 2. Does neighbourhood affect review activity?
SELECT 
    review_activity, 
    neighbourhood_group,
    COUNT(*) AS listing_count,
    ROUND(AVG(number_of_reviews), 2) AS avg_reviews,
    ROUND(AVG(estimated_bookings_month), 2) AS avg_estimated_bookings_month
FROM listings_data_clean
GROUP BY review_activity, neighbourhood_group
ORDER BY
CASE review_activity
    WHEN 'No Reviews' THEN 1
    WHEN 'Low' THEN 2
    WHEN 'Medium' THEN 3
    WHEN 'High' THEN 4
END,
neighbourhood_group DESC;

-- 3. Does higher demand listings get more reviews?
SELECT
    review_activity,
    COUNT(*) AS listing_count,
    ROUND(AVG(number_of_reviews), 2) AS avg_reviews,
    ROUND(AVG(estimated_bookings_month), 2) AS avg_estimated_bookings_month
FROM listings_data_clean
GROUP BY review_activity
ORDER BY
CASE review_activity
    WHEN 'No Reviews' THEN 1
    WHEN 'Low' THEN 2
    WHEN 'Medium' THEN 3
    WHEN 'High' THEN 4
END;

-- Room type exploration
-- 1. How does room type differ in price
SELECT
    room_type,
    COUNT(*) AS listing_count,
    ROUND(AVG(price), 2) AS avg_price
FROM listings_data_clean
GROUP BY room_type
ORDER BY avg_price DESC;

-- 2. Which room types have the most demand?
SELECT
    room_type,
    COUNT(*) AS listing_count,
    ROUND(AVG(estimated_bookings_month), 2) AS avg_estimated_bookings_month,
    ROUND(AVG(reviews_per_month), 2) AS avg_reviews_per_month
FROM listings_data_clean
GROUP BY room_type
ORDER BY avg_estimated_bookings_month DESC;

-- 3. How do room types differ in minimum nights required?
SELECT
    room_type,
    COUNT(*) AS listing_count,
    ROUND(AVG(minimum_nights), 2) AS avg_minimum_nights
FROM listings_data_clean
GROUP BY room_type
ORDER BY avg_minimum_nights DESC;