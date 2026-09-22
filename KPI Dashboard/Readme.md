# Retail KPI Dashboard

This project is a single-page Retail KPI Dashboard created using **Looker Studio** and **Google Sheets**.

## Dashboard

[View the Live Looker Studio Dashboard](https://datastudio.google.com/reporting/e5cddab5-82a0-4959-a80b-0e48b3791a3b)

## Project Objective

The objective of this project is to define and monitor key performance indicators (KPIs) for a retail business.

The dashboard provides a single-page view of sales performance, profitability, regional performance, product performance, and KPI status.

## KPI Definitions

| KPI | Formula | Owner | Frequency | Target | Type |
|---|---|---|---|---|---|
| Total Revenue | SUM(Revenue) | Sales Manager | Daily | ≥ ₹75,000/month | Lagging |
| Total Orders | COUNT(Order ID) | Sales Manager | Daily | ≥ 20/month | Lagging |
| Average Order Value | Total Revenue / Total Orders | Sales Manager | Weekly | ≥ ₹30,000 | Lagging |
| Total Quantity Sold | SUM(Quantity) | Sales Manager | Daily | ≥ 100/month | Lagging |
| Gross Profit | Total Revenue - Total Cost | Finance Manager | Monthly | ≥ ₹150,000 | Lagging |
| Gross Profit % | Gross Profit / Total Revenue × 100 | Finance Manager | Monthly | ≥ 25% | Lagging |
| Revenue Growth % | (Current Revenue - Previous Revenue) / Previous Revenue × 100 | Business Manager | Monthly | ≥ 10% | Lagging |
| Order Growth % | (Current Orders - Previous Orders) / Previous Orders × 100 | Sales Manager | Monthly | ≥ 10% | Lagging |
| Product Demand | Product Quantity / Total Quantity × 100 | Product Manager | Weekly | ≥ 5% for key products | Leading |
| Customer Purchase Activity | Number of customer orders | Marketing Manager | Weekly | Increasing trend | Leading |

## Leading vs Lagging Indicators

### Leading Indicators

Leading indicators provide an early indication of future business activity.

- Product Demand
- Customer Purchase Activity

### Lagging Indicators

Lagging indicators measure business results that have already occurred.

- Total Revenue
- Total Orders
- Average Order Value
- Total Quantity Sold
- Gross Profit
- Gross Profit %
- Revenue Growth %
- Order Growth %

## Dashboard KPIs

The dashboard displays the following main KPI cards:

- Total Revenue
- Total Orders
- Average Order Value
- Gross Profit
- Gross Profit %

### KPI Values

The dashboard currently shows:

- **Total Revenue:** 676,500
- **Total Orders:** 20
- **Average Order Value:** 33,825
- **Gross Profit:** 167,000
- **Gross Profit %:** 24.69%

## Dashboard Charts

### 1. Revenue Trend

A line chart showing revenue over time using the `order_date` field.

This helps identify changes and unusual fluctuations in revenue during the reporting period.

### 2. Revenue by Region

A bar chart comparing revenue across different regions:

- North
- South
- East
- West

This helps identify differences in regional sales performance.

### 3. Revenue by Product

A bar chart comparing revenue across products such as:

- Laptop
- Phone
- Table
- Chair
- Shirt
- Jeans
- Mouse

This helps identify products contributing to overall revenue.

### 4. KPI Performance Table

The dashboard contains a KPI table with:

- KPI Name
- Status
- Actual
- Target

The table is used to compare actual KPI performance against predefined targets.

## KPI Status

The dashboard uses defined targets to monitor KPI performance.

The displayed KPIs are currently marked as **On Track** based on the configured targets.

Examples include:

- Average Order Value
- Gross Margin %
- Gross Profit
- Total Orders
- Total Revenue

## KPI Narrative

### Revenue

Total revenue is **676,500**. The Revenue Trend chart provides a view of revenue changes over the reporting period and can be used to identify periods with higher or lower sales.

### Orders

The dashboard records **20 total orders**. Order volume provides an indication of customer purchasing activity.

### Average Order Value

The Average Order Value is **33,825**. It is calculated by dividing total revenue by the total number of orders.

### Gross Profit

Gross profit is shown as **167,000**. Gross profit represents the amount remaining after subtracting costs from revenue.

### Gross Profit %

Gross Profit % is **24.69%**. This KPI measures profitability relative to total revenue.

### Regional Performance

The Revenue by Region chart allows sales performance to be compared across North, South, East, and West regions.

### Product Performance

The Revenue by Product chart shows the contribution of different products to total revenue. Laptop and Phone show higher revenue contributions than several other products in the dashboard.

### Leading Indicators

The leading indicators used in this project are:

- Product Demand
- Customer Purchase Activity

These indicators can provide early information about changes in product and customer activity.

### Lagging Indicators

The lagging indicators used in this project are:

- Total Revenue
- Total Orders
- Average Order Value
- Total Quantity Sold
- Gross Profit
- Gross Profit %
- Revenue Growth %
- Order Growth %

These indicators measure business results that have already occurred.

## Anomalies and Observations

The Revenue Trend chart shows fluctuations in revenue across the reporting period. These changes can be investigated by comparing the Revenue by Region and Revenue by Product charts.

The KPI table shows the configured KPIs as **On Track** against their targets.

The dashboard can be used to investigate unusual revenue changes by examining the affected time period, region, or product.

## Data Source

The dashboard uses a retail sales dataset stored in **Google Sheets**.

The dataset contains:

- Order ID
- Customer
- Region
- Product
- Quantity
- Revenue
- Cost
- Order Date

## Tools Used

- Looker Studio
- Google Sheets
- CSV
- Git
- GitHub

## Project Structure

```text
Retail KPI Dashboard/
│
├── KPI Definitions.md
├── KPI Narrative.md
├── README.md
└── Cynaris_Sales_Dashboard.csv