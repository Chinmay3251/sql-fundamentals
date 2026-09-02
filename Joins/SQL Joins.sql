create database Sales;
Use sales;
CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    product VARCHAR(50),
    amount INT
);
CREATE TABLE employees (
    employee_id INT,
    employee_name VARCHAR(50),
    manager_id INT
);
INSERT INTO customers VALUES
(1, 'Rahul', 'Bangalore'),
(2, 'Priya', 'Mumbai'),
(3, 'Amit', 'Delhi'),
(4, 'Neha', 'Chennai');
INSERT INTO orders VALUES
(101, 1, 'Laptop', 50000),
(102, 1, 'Mouse', 1000),
(103, 2, 'Keyboard', 2000),
(104, 5, 'Monitor', 10000);
INSERT INTO employees VALUES
(1, 'Ravi', NULL),
(2, 'Priya', 1),
(3, 'Amit', 1),
(4, 'Neha', 2);

-- INNER JOIN
SELECT 
	c.customer_name,
    o.product,
    o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- LEFT JOIN
SELECT
    c.customer_name,
    o.product,
    o.amount
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id;

-- RIGHT JOIN
SELECT
    c.customer_name,
    o.product,
    o.amount
FROM customers AS c
RIGHT JOIN orders AS o
ON c.customer_id = o.customer_id;

-- Understand JOIN duplicates
SELECT DISTINCT
    c.customer_name
FROM customers AS c
JOIN orders AS o
ON c.customer_id = o.customer_id;

-- SELF JOIN
SELECT
	e.employee_name,
    m.employee_name
FROM Employees e
LEFT JOIN employees m
ON m.employee_id = e.employee_id;


