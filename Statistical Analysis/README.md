# Statistical Analysis

This project performs descriptive and distribution analysis on a retail sales dataset using Python.

## Project Objective

The objective of this project is to understand the distribution of revenue using descriptive statistics, frequency distributions, percentiles, quartiles, and box plots.

## Dataset

The analysis uses the `Cynaris_Sales_Dashboard.csv` dataset.

The main variable used for statistical analysis is:

- `revenue`

The `region` column is used to compare revenue distributions between two groups.

## Statistical Measures

The following statistical measures were calculated:

- Mean
- Median
- Mode
- Variance
- Standard Deviation
- Percentiles
- Quartiles
- Interquartile Range (IQR)

## Results

| Statistic | Result |
|---|---:|
| Mean Revenue | ₹33,825 |
| Median Revenue | ₹13,500 |
| Q1 (25th Percentile) | ₹8,750 |
| Q2 (50th Percentile) | ₹13,500 |
| Q3 (75th Percentile) | ₹52,500 |
| IQR | ₹43,750 |
| Standard Deviation | ₹34,460.58 |

## Frequency Distribution

A histogram with a KDE curve was created to visualise the revenue distribution.

The distribution is **right-skewed** because most observations have relatively lower revenue values, while a few orders have much higher revenue values.

The generated chart is:

```text
revenue_frequency_distribution.png

About

I created this project to practice descriptive statistics and understand how statistical measures and visualisations can be used to analyse business data.

Author: Chinmay Chindi
B.Tech – Information Technology, Garden City University