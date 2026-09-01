create database Sales;
Use sales;
CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    city VARCHAR(50),
    salesperson VARCHAR(100),
    order_date DATE
);
INSERT INTO sales
(order_id, customer_name, product, category, quantity, price, city, salesperson, order_date)
VALUES
(1, 'Amit Sharma', 'Laptop', 'Electronics', 1, 55000, 'Bangalore', 'Rahul', '2026-01-05'),
(2, 'Priya Singh', 'Mobile Phone', 'Electronics', 2, 25000, 'Mysore', 'Sneha', '2026-01-08'),
(3, 'Arun Kumar', 'Headphones', 'Electronics', 3, 3000, 'Bangalore', 'Rahul', '2026-01-12'),
(4, 'Neha Patel', 'Office Chair', 'Furniture', 2, 8000, 'Chennai', 'Anita', '2026-01-15'),
(5, 'Ravi Kumar', 'T-Shirt', 'Clothing', 4, 1200, 'Bangalore', 'Suresh', '2026-01-18'),
(6, 'Anjali Rao', 'Tablet', 'Electronics', 1, 18000, 'Mysore', NULL, '2026-01-20'),
(7, 'Ajay Verma', 'Sofa', 'Furniture', 1, 30000, 'Hyderabad', 'Anita', '2026-01-22'),
(8, 'Sneha Reddy', 'Jeans', 'Clothing', 2, 2500, 'Chennai', 'Suresh', '2026-01-25'),
(9, 'Kiran Das', 'Smart Watch', 'Electronics', 3, 7000, 'Bangalore', 'Rahul', '2026-01-28'),
(10, 'Anusha Rao', 'Laptop Bag', 'Accessories', 2, 1500, 'Mysore', NULL, '2026-02-02'),
(11, 'Manoj Singh', 'Monitor', 'Electronics', 2, 15000, 'Hyderabad', 'Sneha', '2026-02-05'),
(12, 'Akash Jain', 'Keyboard', 'Electronics', 5, 2000, 'Bangalore', 'Rahul', '2026-02-08'),
(13, 'Divya Nair', 'Dining Table', 'Furniture', 1, 22000, 'Chennai', 'Anita', '2026-02-10'),
(14, 'Arun Patel', 'Shoes', 'Clothing', 2, 4000, 'Mysore', 'Suresh', '2026-02-12'),
(15, 'Meena Shah', 'Printer', 'Electronics', 1, 12000, 'Bangalore', NULL, '2026-02-15');

-- 1. SELECT and FROM
SELECT *
FROM sales;

-- 2. Select specific columns
SELECT customer_name, product, price
FROM sales;

-- 3. WHERE + AND
SELECT *
FROM sales
WHERE category = 'Electronics'
AND price > 10000;

-- 4. WHERE + OR
SELECT *
FROM sales
WHERE city = 'Bangalore'
OR city = 'Mysore';

-- 5. WHERE + NOT
SELECT *
FROM sales
WHERE NOT category = 'Clothing';

-- 6. LIKE
SELECT *
FROM sales
WHERE customer_name LIKE 'A%';

-- 7. IN
SELECT *
FROM sales
WHERE city IN ('Bangalore', 'Mysore', 'Chennai');

-- 8. BETWEEN
SELECT *
FROM sales
WHERE price BETWEEN 5000 AND 20000;

-- 9. IS NULL
SELECT *
FROM sales
WHERE salesperson IS NULL;

-- 10. Combined conditions
SELECT order_id, customer_name, product, price
FROM sales
WHERE quantity > 2
AND price BETWEEN 5000 AND 30000;