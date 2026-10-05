# Data Quality Report

- **Rows:** 100,000
- **Columns:** 12
- **Duplicate rows:** 0

## Column data types

|                 | dtype          |
|:----------------|:---------------|
| order_id        | int64          |
| order_date      | datetime64[ns] |
| state           | object         |
| city            | object         |
| customer_type   | object         |
| product         | object         |
| category        | object         |
| quantity        | int64          |
| unit_price      | int64          |
| payment_method  | object         |
| customer_rating | float64        |
| total_sales     | int64          |

## Missing values

|                 |   missing_count |
|:----------------|----------------:|
| order_id        |               0 |
| order_date      |               0 |
| state           |               0 |
| city            |               0 |
| customer_type   |               0 |
| product         |               0 |
| category        |               0 |
| quantity        |               0 |
| unit_price      |               0 |
| payment_method  |               0 |
| customer_rating |               0 |
| total_sales     |               0 |

## Numeric summary

|       |   order_id |   quantity |   unit_price |   customer_rating |   total_sales |
|:------|-----------:|-----------:|-------------:|------------------:|--------------:|
| count |   100000   |  100000    |     100000   |         100000    |        100000 |
| mean  |    50000.5 |       3.05 |      45912.5 |              3.76 |        139998 |
| std   |    28867.7 |       1.39 |      36279.1 |              0.72 |        138405 |
| min   |        1   |       1    |       1066   |              2.5  |          1250 |
| 25%   |    25000.8 |       2    |      16059   |              3.2  |         39829 |
| 50%   |    50000.5 |       3    |      34426   |              3.8  |         90040 |
| 75%   |    75000.2 |       4    |      67390   |              4.4  |        199335 |
| max   |   100000   |       5    |     148212   |              5    |        741060 |