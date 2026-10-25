-- SQLite
-- Customers With Positive Revenue (NeetCode SQL)
-- Runs as-is in PostgreSQL or SQLite.
 
-- 1. Set up the table
DROP TABLE IF EXISTS customers;
 
CREATE TABLE customers (
    customer_id INT,
    year        INT,
    revenue     INT,
    PRIMARY KEY (customer_id, year)
);
 
-- 2. Sample data (Example 1 from the problem)
INSERT INTO customers (customer_id, year, revenue) VALUES
    (1, 2019, 100),
    (1, 2020,  50),
    (2, 2020, -30),
    (3, 2019,  80),
    (3, 2020,  25);
 
-- 3. Solution
SELECT customer_id
FROM customers
WHERE year = 2020
  AND revenue > 0;
 
-- Expected output:
-- customer_id
-- 1
-- 3
 