import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\Statistical Analysis\\Cynaris_Sales_Dashboard.csv")

# Select revenue for statistical analysis
revenue = df["revenue"]

print("========== STATISTICAL ANALYSIS ==========")

# Mean
print("Mean:", revenue.mean())

# Median
print("Median:", revenue.median())

# Mode
print("Mode:", revenue.mode().tolist())

# Variance
print("Variance:", revenue.var())

# Standard deviation
print("Standard Deviation:", revenue.std())

# Percentiles
print("\n========== PERCENTILES ==========")
print("25th Percentile:", revenue.quantile(0.25))
print("50th Percentile:", revenue.quantile(0.50))
print("75th Percentile:", revenue.quantile(0.75))

# Quartiles
Q1 = revenue.quantile(0.25)
Q2 = revenue.quantile(0.50)
Q3 = revenue.quantile(0.75)

print("\n========== QUARTILES ==========")
print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)

# IQR
IQR = Q3 - Q1

print("IQR:", IQR)

# Frequency distribution
plt.figure(figsize=(8, 5))

sns.histplot(
    revenue,
    bins=8,
    kde=True
)

plt.title("Revenue Frequency Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("revenue_frequency_distribution.png")
plt.show()

# Side-by-side box plots
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df[df["region"].isin(["North", "South"])],
    x="region",
    y="revenue"
)

plt.title("Revenue Distribution: North vs South")
plt.xlabel("Region")
plt.ylabel("Revenue")

plt.tight_layout()
plt.savefig("north_south_boxplot.png")
plt.show()

print("\n========== INTERPRETATION ==========")

print("The revenue distribution is right-skewed because several high-value")
print("orders are much larger than the majority of orders.")

print("Q1 represents the 25th percentile.")
print("Q2 represents the median or 50th percentile.")
print("Q3 represents the 75th percentile.")

print("The box plot compares the spread and median revenue between North and South.")