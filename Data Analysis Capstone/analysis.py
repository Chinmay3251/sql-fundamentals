import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import os

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\Data Analysis Capstone\\telco_churn.csv")

print("========== DATASET LOADED ==========")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# ==========================================
# 2. DATA CLEANING
# ==========================================

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Handle missing TotalCharges
df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# Remove duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

# Remove unnecessary customer ID from analysis
df["SeniorCitizen"] = df["SeniorCitizen"].astype(int)

# Convert Yes/No values
df["Churn_Flag"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})

print("\n========== CLEANED DATA ==========")
print(df.head())

print("\nFinal missing values:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv(
    "cleaned_telco_churn.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")

# ==========================================
# 3. CREATE CHART FOLDER
# ==========================================

os.makedirs("charts", exist_ok=True)

sns.set_theme(style="whitegrid")

# ==========================================
# 4. BASIC STATISTICS
# ==========================================

print("\n========== BASIC STATISTICS ==========")

print("Mean Monthly Charges:",
      round(df["MonthlyCharges"].mean(), 2))

print("Median Monthly Charges:",
      round(df["MonthlyCharges"].median(), 2))

print("Mean Tenure:",
      round(df["tenure"].mean(), 2))

print("Median Tenure:",
      round(df["tenure"].median(), 2))

print("Mean Total Charges:",
      round(df["TotalCharges"].mean(), 2))

# ==========================================
# 5. CHURN ANALYSIS
# ==========================================

churn_count = df["Churn"].value_counts()

print("\n========== CHURN COUNT ==========")
print(churn_count)

churn_rate = df["Churn_Flag"].mean() * 100

print("\nOverall Churn Rate:",
      round(churn_rate, 2), "%")

# ==========================================
# 6. CHURN BY CONTRACT
# ==========================================

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print("\n========== CHURN BY CONTRACT ==========")
print(contract_churn)

# ==========================================
# 7. CHURN BY PAYMENT METHOD
# ==========================================

payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100

print("\n========== CHURN BY PAYMENT METHOD ==========")
print(payment_churn)

# ==========================================
# 8. CHURN BY TENURE
# ==========================================

tenure_churn = df.groupby("Churn")["tenure"].mean()

print("\n========== TENURE BY CHURN ==========")
print(tenure_churn)

# ==========================================
# 9. CHURN BY MONTHLY CHARGES
# ==========================================

charges_churn = df.groupby("Churn")[
    "MonthlyCharges"
].mean()

print("\n========== MONTHLY CHARGES BY CHURN ==========")
print(charges_churn)

# ==========================================
# 10. VISUALISATION
# ==========================================

# Churn Distribution

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Churn"
)

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "charts/churn_distribution.png"
)

plt.show()


# Churn by Contract

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Contract",
    hue="Churn"
)

plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.tight_layout()

plt.savefig(
    "charts/churn_by_contract.png"
)

plt.show()


# Churn by Payment Method

plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x="PaymentMethod",
    hue="Churn"
)

plt.title("Customer Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "charts/churn_by_payment.png"
)

plt.show()


# Churn by Tenure

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="tenure"
)

plt.title("Tenure Distribution by Churn")
plt.xlabel("Churn")
plt.ylabel("Tenure (Months)")

plt.tight_layout()

plt.savefig(
    "charts/churn_by_tenure.png"
)

plt.show()


# Monthly Charges by Churn

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Churn",
    y="MonthlyCharges"
)

plt.title("Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")

plt.tight_layout()

plt.savefig(
    "charts/churn_by_monthly_charges.png"
)

plt.show()


# ==========================================
# 11. CORRELATION ANALYSIS
# ==========================================

numeric_columns = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "Churn_Flag"
]

correlation_matrix = df[
    numeric_columns
].corr()

print("\n========== CORRELATION MATRIX ==========")
print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Customer Churn Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    "charts/correlation_heatmap.png"
)

plt.show()


# ==========================================
# 12. PEARSON CORRELATION
# ==========================================

correlation, p_value = pearsonr(
    df["tenure"],
    df["Churn_Flag"]
)

print("\n========== PEARSON CORRELATION ==========")

print(
    "Tenure vs Churn correlation:",
    round(correlation, 4)
)

print(
    "P-value:",
    round(p_value, 4)
)


# ==========================================
# 13. KEY BUSINESS INSIGHTS
# ==========================================

print("\n========== KEY BUSINESS INSIGHTS ==========")

print(
    "1. Customers with shorter tenure show higher churn."
)

print(
    "2. Contract type is associated with different churn levels."
)

print(
    "3. Monthly charges differ between churned and retained customers."
)

print(
    "4. Payment method is associated with different churn patterns."
)

print(
    "5. Customer tenure and churn show a measurable relationship."
)

print("\n==========================================")
print("END-TO-END CUSTOMER CHURN ANALYSIS COMPLETE")
print("==========================================")