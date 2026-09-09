import pandas as pd


# ==========================================
# 1. CREATE TWO DATAFRAMES
# ==========================================

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "customer_name": ["Rahul", "Priya", "Amit", "Neha", "Ravi"],
    "city": ["Bangalore", "Mumbai", "Delhi", "Chennai", "Pune"]
})

orders = pd.DataFrame({
    "customer_id": [1, 2, 2, 4, 6],
    "product": ["Laptop", "Chair", "Table", "Phone", "Monitor"],
    "amount": [50000, 2000, 5000, 20000, 10000]
})


# ==========================================
# 2. INNER JOIN
# ==========================================

inner_join = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="inner"
)

print("\nINNER JOIN")
print(inner_join)


# ==========================================
# 3. LEFT JOIN
# ==========================================

left_join = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left"
)

print("\nLEFT JOIN")
print(left_join)


# ==========================================
# 4. RIGHT JOIN
# ==========================================

right_join = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="right"
)

print("\nRIGHT JOIN")
print(right_join)


# ==========================================
# 5. OUTER JOIN
# ==========================================

outer_join = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="outer"
)

print("\nOUTER JOIN")
print(outer_join)


# ==========================================
# 6. LOAD SALES DATA
# ==========================================

sales = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\Python Pandas Advanced\\sales.csv")

# Create sales amount
sales["sales_amount"] = sales["quantity"] * sales["price"]

print("\nSALES DATA")
print(sales)


# ==========================================
# 7. PIVOT TABLE
# ==========================================

pivot_table = pd.pivot_table(
    sales,
    values="sales_amount",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0
)

print("\nPIVOT TABLE")
print(pivot_table)


# ==========================================
# 8. MELT - WIDE TO LONG FORMAT
# ==========================================

wide_data = pd.DataFrame({
    "region": ["South", "North", "East"],
    "Laptop": [50000, 0, 50000],
    "Phone": [0, 20000, 0],
    "Chair": [0, 2000, 0]
})

print("\nWIDE DATA")
print(wide_data)


long_data = pd.melt(
    wide_data,
    id_vars=["region"],
    var_name="product",
    value_name="sales"
)

print("\nLONG DATA AFTER MELT")
print(long_data)


# ==========================================
# 9. METHOD CHAINING
# ==========================================

result = (
    sales
    .assign(total_sales=lambda x: x["quantity"] * x["price"])
    .groupby("region", as_index=False)
    .agg(
        total_sales=("total_sales", "sum"),
        total_quantity=("quantity", "sum")
    )
    .sort_values("total_sales", ascending=False)
)

print("\nMETHOD CHAINING RESULT")
print(result)