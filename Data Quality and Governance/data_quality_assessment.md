# Data Quality Assessment

## Dataset

Dataset: Sales Dataset

The dataset contains customer, region, category, quantity, price, and sales information.

## DAMA Data Quality Dimensions

| Dimension | Score / 5 | Assessment |
|---|---:|---|
| Accuracy | 4/5 | Values were checked and obvious data errors were cleaned |
| Completeness | 4/5 | Missing values were identified and handled |
| Consistency | 4/5 | Text casing and whitespace were standardised |
| Timeliness | 3/5 | Dataset is suitable for analysis but does not contain a data refresh timestamp |
| Validity | 4/5 | Quantity and price values were checked against reasonable ranges |
| Uniqueness | 5/5 | Duplicate records were identified and removed |

## Overall Score

**24 / 30**

## Summary

The dataset has good overall data quality after cleaning. The main improvements were handling missing values, removing duplicate records, standardising text values, and checking outliers.

Timeliness received a lower score because the dataset does not contain information about when the data was last refreshed.

## Recommendations

- Add a data refresh timestamp.
- Continue checking for duplicate records.
- Validate quantity and price ranges during data ingestion.
- Standardise customer and category values before loading data into reporting systems.
- Run automated data quality checks before the dataset is used by BI dashboards.