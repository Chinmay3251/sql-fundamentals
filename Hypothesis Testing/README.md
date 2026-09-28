Dataset

The analysis uses the Cynaris_Sales_Dashboard.csv retail sales dataset.

The main variables used are:

Revenue
Quantity
Region
Hypothesis Tests
1. Average Revenue

Null Hypothesis (H₀):
Mean revenue = ₹30,000

Alternative Hypothesis (H₁):
Mean revenue ≠ ₹30,000

Result:

T-statistic: 0.4838
P-value: 0.6340
95% Confidence Interval: ₹17,277.97 – ₹50,372.03

Since the p-value is greater than 0.05, the null hypothesis was not rejected.

2. North vs South Revenue

Null Hypothesis (H₀):
Mean North revenue = Mean South revenue

Alternative Hypothesis (H₁):
Mean North revenue ≠ Mean South revenue

Result:

North mean revenue: ₹52,500
South mean revenue: ₹40,666.67
T-statistic: 0.4975
P-value: 0.6301

The p-value is greater than 0.05, so there is not enough evidence to conclude that the average revenue differs between North and South.

3. Average Quantity

Null Hypothesis (H₀):
Mean quantity = 3

Alternative Hypothesis (H₁):
Mean quantity ≠ 3

Result:

T-statistic: 2.6010
P-value: 0.0175

Since the p-value is less than 0.05, the null hypothesis was rejected.

There is statistical evidence that the average quantity is different from 3 units.

P-Value Interpretation

A significance level of 0.05 was used.

p-value < 0.05 → Reject the null hypothesis
p-value ≥ 0.05 → Fail to reject the null hypothesis
Type I Error

A Type I error occurs when a true null hypothesis is rejected.

Business example:
Concluding that North and South have different average revenue when there is actually no real difference.

This could result in unnecessary changes to sales strategies or resource allocation.

Type II Error

A Type II error occurs when a false null hypothesis is not rejected.

Business example:
Concluding that North and South have similar revenue when a real difference exists.

This could cause the business to miss an opportunity to improve performance in a lower-performing region.

Tools Used
Python
Pandas
SciPy
VS Code
Git
GitHub
About

I created this project to practice hypothesis testing and understand how statistical tests can be used to support data-driven business analysis.

Author: Chinmay Chindi
B.Tech – Information Technology, Garden City University