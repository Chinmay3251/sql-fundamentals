import pandas as pd

input_file = "C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_data.csv"
output_file = "C:\\Users\\MSI\\Desktop\\Internship\\DuckDB and Polars\\indian_retail_100k.csv"

df = pd.read_csv(input_file)

# Repeat the existing data until we reach 100,000 rows
repeat_count = (100000 // len(df)) + 1

large_df = pd.concat(
    [df] * repeat_count,
    ignore_index=True
).head(100000)

# Create unique order IDs
large_df["order_id"] = range(1, 100001)

large_df.to_csv(output_file, index=False)

print("100k dataset created successfully!")
print("Rows:", len(large_df))
print("Columns:", len(large_df.columns))
print("File:", output_file)