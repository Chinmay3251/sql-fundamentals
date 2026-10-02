# DuckDB and Polars Analytics

This project compares **Pandas, DuckDB, and Polars** using a 100,000-row Indian retail sales dataset.

## Objectives

- Load a 100k-row CSV into DuckDB
- Run five analytical SQL queries
- Benchmark DuckDB against Pandas
- Run the same operations using Polars
- Compare syntax and performance
- Document the strengths and use cases of each tool

## Dataset

The dataset contains 100,000 Indian retail sales records with information such as:

- Order ID
- Order Date
- State
- City
- Customer Type
- Product
- Category
- Quantity
- Unit Price
- Payment Method
- Customer Rating
- Total Sales

## Analytical Operations

The following operations were performed:

1. Total Sales
2. Average Sales
3. Sales by Category
4. Sales by State
5. Top 10 Products

## Tools Used

- Python
- Pandas
- DuckDB
- Polars
- SQL
- VS Code
- Git
- GitHub

## Files

```text
DuckDB and Polars/
│
├── indian_data.csv
├── indian_retail_100k.csv
├── create_100k.py
├── duckdb_analysis.py
├── pandas_benchmark.py
├── polars_analysis.py
├── benchmark_results.md
├── comparison.md
└── README.md