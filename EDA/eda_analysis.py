import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = sns.load_dataset("titanic")

print("Dataset loaded successfully!")


# ==========================================
# 2. CREATE CHARTS FOLDER
# ==========================================

os.makedirs("charts", exist_ok=True)


# ==========================================
# 3. BASIC DATA PROFILING
# ==========================================

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== NULL VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

print("\n========== FIRST 5 ROWS ==========")
print(df.head())


# ==========================================
# 4. SUMMARY STATISTICS
# ==========================================

summary = df.describe()

print("\n========== SUMMARY STATISTICS ==========")
print(summary)

summary.to_csv("summary_statistics.csv")


# ==========================================
# 5. NUMERIC COLUMNS
# ==========================================

numeric_columns = df.select_dtypes(
    include="number"
).columns

print("\n========== NUMERIC COLUMNS ==========")
print(numeric_columns)


# ==========================================
# 6. DISTRIBUTION OF ALL NUMERIC COLUMNS
# ==========================================

for column in numeric_columns:

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df[column].dropna(),
        kde=True
    )

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        f"charts/distribution_{column}.png"
    )

    plt.show()


# ==========================================
# 7. CORRELATION HEATMAP
# ==========================================

correlation = df[numeric_columns].corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("charts/correlation_heatmap.png")

plt.show()


# ==========================================
# 8. INSIGHT 1 - SURVIVAL BY GENDER
# ==========================================

gender_survival = df.groupby("sex")["survived"].mean()

plt.figure(figsize=(7, 5))

gender_survival.plot(
    kind="bar"
)

plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/survival_by_gender.png")

plt.show()


# ==========================================
# 9. INSIGHT 2 - SURVIVAL BY CLASS
# ==========================================

class_survival = df.groupby("pclass")["survived"].mean()

plt.figure(figsize=(7, 5))

class_survival.plot(
    kind="bar"
)

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/survival_by_class.png")

plt.show()


# ==========================================
# 10. INSIGHT 3 - AGE DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="age",
    hue="survived",
    kde=True
)

plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.tight_layout()

plt.savefig("charts/age_survival.png")

plt.show()


# ==========================================
# 11. INSIGHT 4 - FARE BY CLASS
# ==========================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="pclass",
    y="fare"
)

plt.title("Fare Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")

plt.tight_layout()

plt.savefig("charts/fare_by_class.png")

plt.show()


# ==========================================
# 12. INSIGHT 5 - FAMILY SIZE AND SURVIVAL
# ==========================================

df["family_size"] = (
    df["sibsp"] +
    df["parch"] +
    1
)

family_survival = df.groupby(
    "family_size"
)["survived"].mean()

plt.figure(figsize=(9, 5))

family_survival.plot(
    kind="bar"
)

plt.title("Survival Rate by Family Size")
plt.xlabel("Family Size")
plt.ylabel("Survival Rate")

plt.tight_layout()

plt.savefig("charts/survival_by_family_size.png")

plt.show()


# ==========================================
# 13. FINAL MESSAGE
# ==========================================

print("\n====================================")
print("EDA COMPLETED SUCCESSFULLY!")
print("====================================")

print("\nCharts saved inside the charts folder.")
print("Summary statistics saved as summary_statistics.csv")