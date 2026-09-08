import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\Python Data Visualization\\sales.csv")

print(df)

# Apply Seaborn theme
sns.set_theme(style="whitegrid")

# Create charts folder
import os
os.makedirs("charts", exist_ok=True)


# -------------------------
# 1. LINE CHART
# -------------------------

monthly_sales = df.groupby("month")["sales"].sum()

plt.figure(figsize=(8, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("charts/line_chart.png")
plt.show()


# -------------------------
# 2. BAR CHART
# -------------------------

category_sales = df.groupby("category")["sales"].sum()

plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.savefig("charts/bar_chart.png")
plt.show()


# -------------------------
# 3. SCATTER PLOT
# -------------------------

plt.figure(figsize=(8, 5))

plt.scatter(df["quantity"], df["sales"])

plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.savefig("charts/scatter_chart.png")
plt.show()


# -------------------------
# 4. HISTOGRAM
# -------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["sales"], bins=6)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.savefig("charts/histogram.png")
plt.show()


# -------------------------
# 5. BOX PLOT
# -------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(x=df["sales"])

plt.title("Sales Distribution and Outliers")
plt.xlabel("Sales")

plt.savefig("charts/boxplot.png")
plt.show()
