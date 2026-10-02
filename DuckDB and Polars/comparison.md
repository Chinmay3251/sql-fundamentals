# Pandas vs DuckDB vs Polars

| Criteria | Pandas | DuckDB | Polars |
|---|---|---|---|
| Syntax | Python/DataFrame | SQL | DataFrame/Expression |
| Ease of use | Easy for Python users | Easy for SQL users | Moderate |
| Large dataset processing | Good, but memory dependent | Efficient analytical processing | Fast and memory efficient |
| SQL support | No native SQL | Excellent | Limited compared with DuckDB |
| Best use case | General Python data analysis | SQL analytics on files and datasets | Fast DataFrame processing |

## Speed Comparison

For this 100,000-row local benchmark:

- Pandas was very fast for individual operations after the CSV had already been loaded.
- Polars performed well across the tested DataFrame operations.
- DuckDB provided convenient SQL analytics directly on the CSV.
- The first DuckDB query had additional CSV reading/parsing overhead.

## Syntax Comparison

### Pandas

```python
df.groupby("category")["total_sales"].sum()