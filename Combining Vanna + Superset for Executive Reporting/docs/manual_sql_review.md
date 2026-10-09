# Manual review checklist for 10 NL queries

These test questions assume tables `products`, `orders`, and `order_items`. Confirm your actual schema and edit the training examples/allowlist before testing.

| # | Question | Manually verify |
|---|---|---|
| 1 | Show all products | Correct table/columns; sensible limit |
| 2 | Which products are low in stock? | `stock < 10`; correct stock and product columns |
| 3 | Show the 10 most expensive products | Price descending; limit 10 |
| 4 | How many orders are there? | `COUNT(*)` from orders |
| 5 | What are the top 10 products by quantity sold? | Correct join; SUM quantity; group per product; descending sort |
| 6 | List products with stock below 5 | Uses `< 5`, not `<= 5` |
| 7 | Show products sorted by name | Correct name column and ORDER BY |
| 8 | Count the number of products | COUNT from products |
| 9 | Show the 5 products with the lowest stock | Stock ascending; limit 5 |
| 10 | Show total quantity sold for each product | SUM(quantity), correct join and grouping |

Record the real generated SQL, manual review, and execution result in `manual_test_results.csv`. These are test cases, not claimed successful live runs.
