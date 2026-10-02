import polars as pl
import time

CSV_FILE = "C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv"

df = pl.read_csv(CSV_FILE)

print("========== POLARS ANALYSIS ==========")
print("Rows:", df.height)

operations = {}

# 1. Total Sales
start = time.perf_counter()

total_sales = df.select(
    pl.col("total_sales").sum()
)

operations["1. Total Sales"] = time.perf_counter() - start
print("\nTotal Sales:")
print(total_sales)

# 2. Average Sales
start = time.perf_counter()

average_sales = df.select(
    pl.col("total_sales").mean()
)

operations["2. Average Sales"] = time.perf_counter() - start
print("\nAverage Sales:")
print(average_sales)

# 3. Sales by Category
start = time.perf_counter()

category_sales = (
    df.group_by("category")
    .agg(
        pl.col("total_sales").sum().alias("total_sales")
    )
    .sort("total_sales", descending=True)
)

operations["3. Sales by Category"] = time.perf_counter() - start
print("\nSales by Category:")
print(category_sales)

# 4. Sales by State
start = time.perf_counter()

state_sales = (
    df.group_by("state")
    .agg(
        pl.col("total_sales").sum().alias("total_sales")
    )
    .sort("total_sales", descending=True)
    .head(10)
)

operations["4. Sales by State"] = time.perf_counter() - start
print("\nTop States:")
print(state_sales)

# 5. Top 10 Products
start = time.perf_counter()

product_sales = (
    df.group_by("product")
    .agg([
        pl.col("total_sales").sum().alias("total_sales"),
        pl.col("quantity").sum().alias("total_quantity")
    ])
    .sort("total_sales", descending=True)
    .head(10)
)

operations["5. Top 10 Products"] = time.perf_counter() - start
print("\nTop Products:")
print(product_sales)

print("\n========== POLARS BENCHMARK ==========")

for name, elapsed in operations.items():
    print(f"{name}: {elapsed:.6f} seconds")