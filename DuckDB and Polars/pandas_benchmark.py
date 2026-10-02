import pandas as pd
import time

CSV_FILE = "C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv"

df = pd.read_csv(CSV_FILE)

print("========== PANDAS ANALYSIS ==========")
print("Rows:", len(df))

operations = {}

# 1. Total Sales
start = time.perf_counter()
total_sales = df["total_sales"].sum()
operations["1. Total Sales"] = time.perf_counter() - start
print("\nTotal Sales:", total_sales)

# 2. Average Sales
start = time.perf_counter()
average_sales = df["total_sales"].mean()
operations["2. Average Sales"] = time.perf_counter() - start
print("Average Sales:", average_sales)

# 3. Sales by Category
start = time.perf_counter()
category_sales = (
    df.groupby("category")["total_sales"]
    .sum()
    .sort_values(ascending=False)
)
operations["3. Sales by Category"] = time.perf_counter() - start
print("\nSales by Category:")
print(category_sales)

# 4. Sales by State
start = time.perf_counter()
state_sales = (
    df.groupby("state")["total_sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
operations["4. Sales by State"] = time.perf_counter() - start
print("\nTop States:")
print(state_sales)

# 5. Top 10 Products
start = time.perf_counter()
product_sales = (
    df.groupby("product")
    .agg(
        total_sales=("total_sales", "sum"),
        total_quantity=("quantity", "sum")
    )
    .sort_values("total_sales", ascending=False)
    .head(10)
)
operations["5. Top 10 Products"] = time.perf_counter() - start
print("\nTop Products:")
print(product_sales)

print("\n========== PANDAS BENCHMARK ==========")

for name, elapsed in operations.items():
    print(f"{name}: {elapsed:.6f} seconds")