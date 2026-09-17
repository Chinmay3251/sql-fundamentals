# Power BI DAX Practice

This project contains my practice with DAX functions and concepts in Power BI.

## Practical Tasks

- Used `CALCULATE()` to apply filters to measures
- Created a YTD Sales measure using `DATESYTD()`
- Created a Running Total calculation
- Created a Profit Margin % calculated column
- Learned row context and filter context
- Learned context transition

## DAX Measures

### Total Sales

```DAX
Total Sales =
SUMX(
    'cleaned_sales_powerbi',
    'cleaned_sales_powerbi'[quantity] *
    'cleaned_sales_powerbi'[price]
)
South Sales
South Sales =
CALCULATE(
    [Total Sales],
    'cleaned_sales_powerbi'[region] = "South"
)
YTD Sales
YTD Sales =
CALCULATE(
    [Total Sales],
    DATESYTD('cleaned_sales_powerbi'[order_date])
)
Calculated Columns
Running Total

A running total calculation was created using date-based cumulative sales.

Profit Margin %
Profit Margin % =
DIVIDE(
    'cleaned_sales_powerbi'[profit],
    'cleaned_sales_powerbi'[quantity] *
    'cleaned_sales_powerbi'[price],
    0
)
DAX Concepts
Row Context

Row context means DAX evaluates data one row at a time. Calculated columns commonly use row context.

Filter Context

Filter context determines which rows are included in a calculation based on filters, slicers, or DAX expressions.

Context Transition

Context transition occurs when CALCULATE() converts the current row context into filter context.

Tools Used
Power BI Desktop
DAX
CSV
Git
GitHub
Author

Chinmay Chindi
B.Tech – Information Technology, Garden City University