import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("C:\\Users\\MSI\\Desktop\\Internship\\Hypothesis Testing\\Cynaris_Sales_Dashboard.csv")

# ==========================================
# 1. ONE-SAMPLE T-TEST
# ==========================================

revenue = df["revenue"]

test_value = 30000

t_statistic, p_value = stats.ttest_1samp(
    revenue,
    test_value
)

print("========== ONE-SAMPLE T-TEST ==========")
print("Test value:", test_value)
print("T-statistic:", round(t_statistic, 4))
print("P-value:", round(p_value, 4))

confidence_level = 0.95
alpha = 0.05

mean_revenue = revenue.mean()
standard_error = stats.sem(revenue)

confidence_interval = stats.t.interval(
    confidence_level,
    len(revenue) - 1,
    loc=mean_revenue,
    scale=standard_error
)

print("95% Confidence Interval:", confidence_interval)

if p_value < alpha:
    print("Result: Reject the null hypothesis.")
else:
    print("Result: Fail to reject the null hypothesis.")


# ==========================================
# 2. TWO-SAMPLE T-TEST
# ==========================================

north_revenue = df[df["region"] == "North"]["revenue"]
south_revenue = df[df["region"] == "South"]["revenue"]

t_statistic, p_value = stats.ttest_ind(
    north_revenue,
    south_revenue,
    equal_var=False
)

print("\n========== TWO-SAMPLE T-TEST ==========")
print("North mean revenue:", north_revenue.mean())
print("South mean revenue:", south_revenue.mean())
print("T-statistic:", round(t_statistic, 4))
print("P-value:", round(p_value, 4))

if p_value < alpha:
    print("Result: Reject the null hypothesis.")
    print("There is evidence of a difference between the two groups.")
else:
    print("Result: Fail to reject the null hypothesis.")
    print("There is not enough evidence of a difference between the two groups.")


# ==========================================
# 3. SECOND ONE-SAMPLE T-TEST
# ==========================================

quantity = df["quantity"]

test_quantity = 3

t_statistic, p_value = stats.ttest_1samp(
    quantity,
    test_quantity
)

print("\n========== QUANTITY ONE-SAMPLE T-TEST ==========")
print("Test value:", test_quantity)
print("T-statistic:", round(t_statistic, 4))
print("P-value:", round(p_value, 4))

if p_value < alpha:
    print("Result: Reject the null hypothesis.")
else:
    print("Result: Fail to reject the null hypothesis.")


# ==========================================
# 4. TYPE I AND TYPE II ERRORS
# ==========================================

print("\n========== TYPE I AND TYPE II ERRORS ==========")

print("""
Type I Error:
Rejecting the null hypothesis when it is actually true.

Business consequence:
A company may conclude that two regions have different
sales performance when there is actually no real difference.
This could lead to unnecessary business changes.

Type II Error:
Failing to reject the null hypothesis when it is actually false.

Business consequence:
A company may conclude that two regions have similar
sales performance when a real difference exists.
This could cause the company to miss an important
business opportunity.
""")

print("\n========================================")
print("HYPOTHESIS TESTING COMPLETED")
print("========================================")