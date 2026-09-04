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

-- Write a non-correlated subquery to find above-average sales
SELECT
    sale_id,
    region,
    product,
    quantity * price AS sales_amount
FROM sale
WHERE quantity * price > (
    SELECT AVG(quantity * price)
    FROM sale
);

-- Write a correlated subquery to find the top performer per region
SELECT
    s1.sale_id,
    s1.region,
    s1.product,
    s1.quantity * s1.price AS sales_amount
FROM sale AS s1
WHERE s1.quantity * s1.price = (
    SELECT MAX(s2.quantity * s2.price)
    FROM sale AS s2
    WHERE s2.region = s1.region
);

-- Rewrite a nested subquery as a CTE using the WITH clause
WITH regional_sales AS (
    SELECT
        region,
        SUM(quantity * price) AS total_sales
    FROM sale
    GROUP BY region
)
SELECT
    region,
    total_sales
FROM regional_sales
WHERE total_sales > (
    SELECT AVG(total_sales)
    FROM regional_sales
);

-- Chain 2 CTEs in a single query
WITH regional_sales AS (
    SELECT
        region,
        SUM(quantity * price) AS total_sales
    FROM sale
    GROUP BY region
),
average_sales AS (
    SELECT
        AVG(total_sales) AS avg_region_sales
    FROM regional_sales
)
SELECT
    r.region,
    r.total_sales
FROM regional_sales AS r
CROSS JOIN average_sales AS a
WHERE r.total_sales > a.avg_region_sales;
