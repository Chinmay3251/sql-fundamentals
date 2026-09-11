import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\DATA cleaning\\sales_dirty.csv")

print("========== ORIGINAL DATA ==========")
print(df)

# --------------------------------------------------
# 1. Identify missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Impute missing quantity using median
df["quantity"] = df["quantity"].fillna(df["quantity"].median())

# --------------------------------------------------
# 2. Detect duplicate rows
# --------------------------------------------------

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# --------------------------------------------------
# 3. Standardise string values
# --------------------------------------------------

# Remove extra spaces
df["customer"] = df["customer"].str.strip()
df["region"] = df["region"].str.strip()
df["category"] = df["category"].str.strip()

# Standardise casing
df["customer"] = df["customer"].str.title()
df["region"] = df["region"].str.title()
df["category"] = df["category"].str.title()

# --------------------------------------------------
# 4. Fix known inconsistent customer name
# --------------------------------------------------

df["customer"] = df["customer"].replace({
    "Rahul": "Rahul"
})

# --------------------------------------------------
# 5. Detect outliers using IQR
# --------------------------------------------------

Q1 = df["quantity"].quantile(0.25)
Q3 = df["quantity"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\n========== IQR VALUES ==========")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = df[
    (df["quantity"] < lower_bound) |
    (df["quantity"] > upper_bound)
]

print("\n========== OUTLIERS ==========")
print(outliers)

# Cap outliers instead of removing them
df["quantity"] = df["quantity"].clip(
    lower=lower_bound,
    upper=upper_bound
)

# --------------------------------------------------
# 6. Create sales amount
# --------------------------------------------------

df["sales_amount"] = df["quantity"] * df["price"]

# --------------------------------------------------
# 7. Final data quality check
# --------------------------------------------------

print("\n========== FINAL MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== FINAL DUPLICATES ==========")
print(df.duplicated().sum())

print("\n========== CLEANED DATA ==========")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_sales.csv", index=False)

print("\nCleaned dataset saved as cleaned_sales.csv")