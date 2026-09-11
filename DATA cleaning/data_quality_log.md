# Data Quality Log

## Dataset
Sales dataset containing customer, region, category, quantity, and price information.

## Cleaning Performed

| Issue | Action Taken | Reason |
|---|---|---|
| Missing quantity | Median imputation | Median is less affected by extreme values |
| Duplicate rows | Removed duplicates | Prevent duplicate records from affecting analysis |
| Extra whitespace | Removed using `str.strip()` | Standardise text values |
| Different casing | Converted to title case | Maintain consistent formatting |
| Outliers in quantity | Detected using IQR | Identify unusually high or low values |
| Outliers | Capped using IQR bounds | Keep the record while reducing extreme impact |

## Missing Values

Missing values were identified using:

`isnull().sum()`

The missing quantity value was replaced using the median of the quantity column.

## Duplicate Records

Duplicate records were identified using:

`duplicated().sum()`

Duplicate rows were removed using:

`drop_duplicates()`

## Outlier Detection

The IQR method was used.

- Q1 = 25th percentile
- Q3 = 75th percentile
- IQR = Q3 - Q1
- Lower Bound = Q1 - 1.5 × IQR
- Upper Bound = Q3 + 1.5 × IQR

Outliers in the quantity column were capped using the IQR boundaries.

## String Standardisation

The following columns were cleaned:

- Customer
- Region
- Category

Extra whitespace was removed and text casing was standardised.

## Final Result

The dataset was cleaned and saved as:

`cleaned_sales.csv`

The cleaned dataset is ready for further analysis.