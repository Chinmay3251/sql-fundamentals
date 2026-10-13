# Manual Pandas reference answers

**Dataset disclosure:** This CSV is synthetic/generated for practice, not a real published dataset. Answers below are deterministic Pandas results, not PandasAI output.

## Q01: What is the total revenue in INR?

1724285.0

## Q02: Which 5 products generated the highest revenue?

product
Wireless Earbuds    510405.0
Sports Shoes        400440.0
Pressure Cooker     349920.0
Cotton Saree        330750.0
Tea Powder           51362.5
Name: revenue_inr, dtype: float64

## Q03: Which city has the highest total revenue?

city
Mumbai    249841.0
Name: revenue_inr, dtype: float64

## Q04: What is the total quantity sold by category?

category
Electronics    477
Grocery        454
Clothing       250
Kitchen        233
Stationery     194
Footwear       178
Name: quantity, dtype: int64

## Q05: Which payment method is used most often?

payment_method
Credit Card    134
Name: count, dtype: int64

## Q06: What is the average order revenue?

2873.81

## Q07: What are monthly revenues for 2025?

order_date
2025-01    141151.0
2025-02    172424.5
2025-03    150072.5
2025-04    109517.0
2025-05    102604.5
2025-06    138583.0
2025-07    159735.0
2025-08    189702.5
2025-09    154136.5
2025-10    144884.5
2025-11    128265.0
2025-12    133209.0
Freq: M, Name: revenue_inr, dtype: float64

## Q08: Which region has the highest number of orders?

region
South    234
West     175
North    127
East      64
dtype: int64

## Q09: What percentage of orders used a discount?

57.89

## Q10: Compare revenue from new and returning customers.

customer_type
New          866475.5
Returning    857809.5
Name: revenue_inr, dtype: float64