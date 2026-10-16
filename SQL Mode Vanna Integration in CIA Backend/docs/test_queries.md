# Ten natural-language query test cases

Use these questions after connecting Vanna to the actual schema. **Do not assume the proposed SQL is correct for your database.** Record generated SQL and manually verify table/column names, joins, filters, aggregation, duplicates, NULL behavior, date semantics, and expected results.

1. Which products are low in stock?
2. What are total sales by month?
3. Which are the top 5 products by quantity sold?
4. How many orders were placed?
5. What is the average order value?
6. Which region has the highest sales?
7. Show the number of orders per customer.
8. Which products have never been ordered?
9. What were total sales during the previous calendar month?
10. Which order items have a quantity greater than 3?

## Review record template

For each question, record:
- Generated SQL
- Are table and column names valid? (Yes/No)
- Are joins and join keys correct? (Yes/No)
- Are filters and date boundaries correct? (Yes/No/Not applicable)
- Are aggregates and grouping correct? (Yes/No/Not applicable)
- Does it run against a read-only test database? (Yes/No/Not tested)
- Notes/correction
