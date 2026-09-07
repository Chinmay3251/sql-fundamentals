import pandas as pd

# Load CSV
df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\Python for Data — Pandas Basics\\sales.csv")

# Inspect data
print(df.head())
print(df.info())
print(df.describe())
print(df["region"].value_counts())

# Select columns
print(df[["customer", "region", "category"]])

# Filter rows
south_sales = df[df["region"] == "South"]
print(south_sales)

# Handle missing values
print(df.isnull().sum())
df = df.dropna()

# Create sales amount
df["sales_amount"] = df["quantity"] * df["price"]

# Group by region
summary = df.groupby("region").agg(
    total_quantity=("quantity", "sum"),
    average_price=("price", "mean"),
    number_of_orders=("order_id", "count")
)

print(summary)

# Export cleaned data
df.to_csv("cleaned_sales.csv", index=False)