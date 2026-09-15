# PII Classification

## Dataset

Sales Dataset

## PII Assessment

| Column | PII? | Classification | Risk | Recommended Strategy |
|---|---|---|---|---|
| order_id | No | Business identifier | Low | Keep as-is |
| customer | Yes | Direct personal identifier | Medium | Tokenisation or masking |
| region | No | General location | Low | Keep as-is |
| category | No | Business information | Low | Keep as-is |
| quantity | No | Transaction information | Low | Keep as-is |
| price | No | Transaction information | Low | Keep as-is |
| sales_amount | No | Transaction information | Low | Keep as-is |

## PII Column

### customer

The `customer` column contains customer names and can be used to identify an individual.

Therefore, it should be treated as PII.

## Recommended Strategy

For the BI dashboard, the actual customer name should not normally be exposed.

Instead, use tokenisation.

Example:

```text
Rahul → CUST_001
Priya → CUST_002
Amit → CUST_003