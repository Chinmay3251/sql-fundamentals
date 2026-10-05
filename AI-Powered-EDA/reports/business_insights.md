# AI-Powered Business Insights

> The script computed the metrics from the CSV. Ollama was unavailable, so a transparent rule-based narrative was generated instead.

## Computed metrics

```json
{
  "row_count": 100000,
  "total_sales": 13999802964.0,
  "average_transaction_sales": 139998.02964,
  "total_quantity": 305339,
  "category_sales": {
    "Electronics": 13325274437.0,
    "Office Equipment": 674528527.0
  },
  "top_5_states": {
    "Tamil Nadu": 1557005706.0,
    "Delhi": 1552171180.0,
    "West Bengal": 1538644833.0,
    "Karnataka": 1525878685.0,
    "Gujarat": 1483521906.0
  },
  "top_5_products": {
    "Television": 3500571030.0,
    "Laptop": 2912484013.0,
    "Camera": 2789400833.0,
    "Smartphone": 1778394399.0,
    "Tablet": 1398799958.0
  },
  "highest_sales_month": "2025-10",
  "lowest_sales_month": "2025-08",
  "average_customer_rating": 3.759000000000001
}
```

## Data-backed observations

- The dataset contains **100,000 rows** and total recorded sales of **13,999,802,964.00**.
- Average sales per row are **139,998.03**.
- **Electronics** is the highest-sales category in the supplied data.
- **Tamil Nadu** is the highest-sales state among the grouped results.
- **Television** is the highest-sales product in the grouped results.
- The highest-sales month is **2025-10** and the lowest-sales month is **2025-08**.
- Average customer rating is **3.76**.

## Recommendations to investigate

- Review inventory and supplier planning for the highest-sales products.
- Compare state-level sales with customer counts, marketing spend, and delivery costs before reallocating budgets.
- Investigate lower-sales categories and months to determine whether seasonality, stock availability, or product mix may explain the pattern.
- Track customer ratings alongside sales to check whether customer experience differs by product, category, or state.

## Interpretation note

These recommendations are hypotheses for further investigation, not proof of cause and effect. Validate them with additional business data before making decisions.

> Important: the source dataset is a practice dataset and the 100k-row version was expanded by repeating rows. Treat the findings as a demonstration, not as independent real-world market evidence.
