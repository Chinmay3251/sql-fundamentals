import duckdb
import time

CSV_FILE = "C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv"

con = duckdb.connect()

print("========== DUCKDB ANALYSIS ==========")

queries = {
    "1. Total Sales":
        "SELECT SUM(total_sales) AS total_sales FROM read_csv_auto('C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv')",

    "2. Average Sales":
        "SELECT AVG(total_sales) AS average_sales FROM read_csv_auto('C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv')",

    "3. Sales by Category":
        """
        SELECT category, SUM(total_sales) AS total_sales
        FROM read_csv_auto('C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv')
        GROUP BY category
        ORDER BY total_sales DESC
        """,

    "4. Sales by State":
        """
        SELECT state, SUM(total_sales) AS total_sales
        FROM read_csv_auto('C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv')
        GROUP BY state
        ORDER BY total_sales DESC
        LIMIT 10
        """,

    "5. Top 10 Products":
        """
        SELECT product,
               SUM(total_sales) AS total_sales,
               SUM(quantity) AS total_quantity
        FROM read_csv_auto('C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv')
        GROUP BY product
        ORDER BY total_sales DESC
        LIMIT 10
        """
}

results = {}

for name, query in queries.items():

    start = time.perf_counter()

    result = con.execute(query).fetchdf()

    elapsed = time.perf_counter() - start

    results[name] = elapsed

    print(f"\n{name}")
    print(result)
    print(f"Execution time: {elapsed:.6f} seconds")


print("\n========== DUCKDB BENCHMARK ==========")

for name, elapsed in results.items():
    print(f"{name}: {elapsed:.6f} seconds")

con.close()

print("\nDuckDB analysis completed successfully!")