-- Load the CSV into PostgreSQL first, then create the chart datasets.
-- Replace retail_sales with the actual imported table name if different.

-- 1. Metric: Total Sales
SELECT SUM("Sales") AS total_sales
FROM retail_sales;

-- 2. Bar: Sales by Category
SELECT "Category", SUM("Sales") AS total_sales
FROM retail_sales
GROUP BY "Category"
ORDER BY total_sales DESC;

-- 3. Line: Monthly Sales Trend
SELECT DATE_TRUNC('month', "Order Date") AS month,
       SUM("Sales") AS total_sales
FROM retail_sales
GROUP BY 1
ORDER BY 1;

-- 4. Pie: Sales by Region
SELECT "Region", SUM("Sales") AS total_sales
FROM retail_sales
GROUP BY "Region"
ORDER BY total_sales DESC;

-- 5. Table: Top 10 Products
SELECT "Product Name", SUM("Sales") AS total_sales
FROM retail_sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;
