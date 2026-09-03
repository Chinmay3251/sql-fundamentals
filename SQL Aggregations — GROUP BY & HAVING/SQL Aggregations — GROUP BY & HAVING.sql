USE sales;
CREATE TABLE sale (
    sale_id INT,
    region VARCHAR(50),
    category VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    sale_date DATE
);
INSERT INTO sale VALUES
(1, 'South', 'Electronics', 'Laptop', 2, 50000, '2026-01-10'),
(2, 'North', 'Furniture', 'Chair', 5, 2000, '2026-01-15'),
(3, 'South', 'Electronics', 'Mouse', 10, 500, '2026-02-05'),
(4, 'East', 'Clothing', 'Shirt', 8, 1000, '2026-02-12'),
(5, 'West', 'Furniture', 'Table', 3, 5000, '2026-02-20'),
(6, 'North', 'Electronics', 'Phone', 4, 20000, '2026-03-03'),
(7, 'South', 'Clothing', 'Jeans', 6, 1500, '2026-03-10'),
(8, 'East', 'Electronics', 'Laptop', 1, 50000, '2026-03-15'),
(9, 'West', 'Clothing', 'Shirt', 10, 1000, '2026-04-05'),
(10, 'North', 'Furniture', 'Table', 2, 5000, '2026-04-12');

-- Aggregate Query 1: COUNT
SELECT count(*) AS Total_sales
FROM sale;

-- Aggregate Query 2: SUM
SELECT SUM(quantity) AS total_quantity
FROM sale;

-- Aggregate Query 3: AVG
SELECT AVG(price) AS average_price
FROM sale;

-- Aggregate Query 4: MAX
SELECT MAX(price) AS highest_price
FROM sale;

-- Aggregate Query 5: MIN
SELECT MIN(price) AS lowest_price
FROM sale;

-- Aggregate Query 6: SUM by Region
SELECT
    region,
    SUM(quantity) AS total_quantity
FROM sale
GROUP BY region;

-- Aggregate Query 7: SUM by Category
SELECT
    category,
    SUM(quantity * price) AS total_sales
FROM sale
GROUP BY category;

-- Aggregate Query 8: COUNT by Category
SELECT
    category,
    COUNT(*) AS total_sales
FROM sale
GROUP BY category;

-- Group Sales by Region
SELECT
    region,
    COUNT(*) AS number_of_orders,
    SUM(quantity * price) AS total_sales,
    AVG(price) AS average_price
FROM sale
GROUP BY region;

-- Group Sales by Category
 SELECT
    category,
    COUNT(*) AS number_of_orders,
    SUM(quantity * price) AS total_sales,
    AVG(price) AS average_price
FROM sale
GROUP BY category;

-- Group Sales by Month
SELECT
    DATE_FORMAT(sale_date, '%Y-%m') AS month,
    SUM(quantity * price) AS total_sales
FROM sale
GROUP BY DATE_FORMAT(sale_date, '%Y-%m');

-- Use HAVING
SELECT
    region,
    SUM(quantity * price) AS total_sales
FROM sale
GROUP BY region
HAVING SUM(quantity * price) > 50000;

-- Window Function: SUM OVER()
SELECT
    sale_id,
    region,
    category,
    quantity * price AS sales_amount,
    SUM(quantity * price) OVER() AS total_sales
FROM sale;