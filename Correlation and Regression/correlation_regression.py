import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr, spearmanr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("Cynaris_Sales_Dashboard.csv")

print("========== DATASET ==========")
print(df.head())

print("\nDataset shape:", df.shape)


# ==========================================
# 2. PEARSON AND SPEARMAN CORRELATION
# ==========================================

print("\n========== CORRELATION ANALYSIS ==========")

x = df["cost"]
y = df["revenue"]

pearson_correlation, pearson_pvalue = pearsonr(x, y)
spearman_correlation, spearman_pvalue = spearmanr(x, y)

print("Pearson correlation:", round(pearson_correlation, 4))
print("Spearman correlation:", round(spearman_correlation, 4))

print("\nInterpretation:")
print("Pearson measures the strength of a linear relationship.")
print("Spearman measures the strength of a monotonic relationship.")

if pearson_correlation > 0:
    print("The Pearson correlation is positive.")
else:
    print("The Pearson correlation is negative.")

if abs(pearson_correlation) > 0.7:
    print("The relationship is strong.")
elif abs(pearson_correlation) > 0.3:
    print("The relationship is moderate.")
else:
    print("The relationship is weak.")


# ==========================================
# 3. CORRELATION HEATMAP
# ==========================================

print("\n========== CORRELATION HEATMAP ==========")

numeric_columns = [
    "quantity",
    "revenue",
    "cost"
]

correlation_matrix = df[numeric_columns].corr()

print(correlation_matrix)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig("correlation_heatmap.png")
plt.show()


# ==========================================
# 4. SCATTER MATRIX
# ==========================================

print("\n========== SCATTER MATRIX ==========")

sns.pairplot(
    df[numeric_columns],
    diag_kind="hist"
)

plt.savefig("scatter_matrix.png")
plt.show()


# ==========================================
# 5. LINEAR REGRESSION
# ==========================================

print("\n========== LINEAR REGRESSION ==========")

X = df[["cost"]]
y = df["revenue"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Intercept:", round(model.intercept_, 2))
print("Coefficient:", round(model.coef_[0], 2))

print(
    "\nRegression equation:"
)

print(
    f"Revenue = {model.intercept_:.2f} + "
    f"({model.coef_[0]:.2f} × Cost)"
)


# ==========================================
# 6. MODEL METRICS
# ==========================================

print("\n========== MODEL METRICS ==========")

r2 = r2_score(y_test, y_pred)

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

print("R²:", round(r2, 4))
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))


# ==========================================
# 7. ACTUAL VS PREDICTED
# ==========================================

results = pd.DataFrame({
    "Actual Revenue": y_test.values,
    "Predicted Revenue": y_pred
})

print("\n========== ACTUAL VS PREDICTED ==========")
print(results)


# ==========================================
# 8. REGRESSION PLOT
# ==========================================

plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x="cost",
    y="revenue"
)

plt.title("Linear Regression: Cost vs Revenue")
plt.xlabel("Cost")
plt.ylabel("Revenue")

plt.tight_layout()
plt.savefig("linear_regression.png")
plt.show()


# ==========================================
# 9. RESIDUAL ANALYSIS
# ==========================================

residuals = y_test - y_pred

print("\n========== RESIDUAL ANALYSIS ==========")

print("Residual mean:", round(residuals.mean(), 2))
print(
    "Residual standard deviation:",
    round(residuals.std(), 2)
)

plt.figure(figsize=(8, 5))

plt.scatter(
    y_pred,
    residuals
)

plt.axhline(
    y=0,
    linestyle="--"
)

plt.title("Residual Plot")
plt.xlabel("Predicted Revenue")
plt.ylabel("Residuals")

plt.tight_layout()
plt.savefig("residual_plot.png")
plt.show()


# ==========================================
# 10. RESIDUAL DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.histplot(
    residuals,
    kde=True
)

plt.title("Residual Distribution")
plt.xlabel("Residual")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("residual_distribution.png")
plt.show()


# ==========================================
# 11. Q-Q PLOT
# ==========================================

import scipy.stats as stats

plt.figure(figsize=(8, 5))

stats.probplot(
    residuals,
    dist="norm",
    plot=plt
)

plt.title("Q-Q Plot of Residuals")

plt.tight_layout()
plt.savefig("qq_plot.png")
plt.show()


# ==========================================
# 12. MODEL ASSUMPTIONS
# ==========================================

print("\n========== MODEL ASSUMPTIONS ==========")

print("1. Linearity:")
print("Check the regression and residual plots for a roughly linear relationship.")

print("\n2. Constant variance:")
print("Residuals should have a relatively similar spread across predictions.")

print("\n3. Normality of residuals:")
print("The residual histogram and Q-Q plot should be approximately normal.")

print("\n4. Independence:")
print("Observations should be independent of each other.")

print("\n========================================")
print("CORRELATION AND REGRESSION COMPLETED")
print("========================================")