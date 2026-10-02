# Benchmark Results

## Dataset

- Dataset: Indian Retail Sales
- Rows: 100,000
- Columns: 12
- File: `indian_retail_100k.csv`

## Execution Time Comparison

| Operation | Pandas | DuckDB | Polars |
|---|---:|---:|---:|
| Total Sales | 0.000548 s | 2.383347 s | 0.047348 s |
| Average Sales | 0.000795 s | 0.130646 s | 0.000793 s |
| Sales by Category | 0.014381 s | 0.123655 s | 0.048207 s |
| Sales by State | 0.005996 s | 0.125361 s | 0.004410 s |
| Top 10 Products | 0.013898 s | 0.121608 s | 0.010344 s |

## Observations

- Pandas performed very quickly for these operations because the dataset was already loaded into memory before timing.
- DuckDB provided SQL-based analytical processing directly against the CSV file.
- The first DuckDB query took longer because the CSV had to be read and parsed.
- Polars provided fast DataFrame operations and performed well on grouping and aggregation tasks.
- All three tools produced the same analytical results.

## Benchmark Limitation

The benchmark is not a completely equal comparison because Pandas and Polars load the CSV before the individual operation timers start, while DuckDB reads the CSV as part of each SQL query.

Therefore, the results should be treated as a practical local benchmark rather than a controlled performance test.

## Conclusion

Pandas is convenient for Python-based data analysis. DuckDB is useful when analytical SQL is preferred, especially when working directly with files. Polars provides a fast DataFrame-based alternative for data processing.