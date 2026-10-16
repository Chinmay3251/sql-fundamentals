"""Vanna integration seam.

Vanna's initialization and training API differ across versions/providers. Keep the
approved provider-specific setup here rather than guessing credentials or APIs.
"""
from typing import Protocol

TRAINING_PAIRS = [
    {"question": "Which products are low in stock?", "sql": "SELECT product_id, product_name, stock FROM products WHERE stock < 10 ORDER BY stock ASC"},
    {"question": "What are total sales by month?", "sql": "SELECT DATE_TRUNC('month', o.order_date) AS month, SUM(oi.quantity * oi.unit_price) AS total_sales FROM orders o JOIN order_items oi ON oi.order_id = o.order_id GROUP BY DATE_TRUNC('month', o.order_date) ORDER BY month"},
    {"question": "Which are the top 5 products by quantity sold?", "sql": "SELECT p.product_name, SUM(oi.quantity) AS units_sold FROM products p JOIN order_items oi ON oi.product_id = p.product_id GROUP BY p.product_name ORDER BY units_sold DESC LIMIT 5"},
    {"question": "How many orders were placed?", "sql": "SELECT COUNT(*) AS order_count FROM orders"},
    {"question": "What is the average order value?", "sql": "SELECT AVG(order_total) AS average_order_value FROM (SELECT o.order_id, SUM(oi.quantity * oi.unit_price) AS order_total FROM orders o JOIN order_items oi ON oi.order_id = o.order_id GROUP BY o.order_id) order_values"},
]

class SQLGenerator(Protocol):
    def generate_sql(self, question: str) -> str: ...

class UnconfiguredVannaGenerator:
    """Safe placeholder until the approved Vanna provider is configured."""
    def generate_sql(self, question: str) -> str:
        raise RuntimeError(
            "Vanna provider is not configured. Initialize your approved Vanna model/provider "
            "in src/vanna_service.py, then train it with TRAINING_PAIRS and your schema."
        )

# Replace this adapter with the Vanna version/provider approved for your project.
generator: SQLGenerator = UnconfiguredVannaGenerator()

def train_examples(vanna_client) -> int:
    """Train a configured Vanna client with the five examples above.

    The caller must provide a compatible client exposing train(question=..., sql=...).
    Verify this method signature against the installed Vanna version.
    """
    for pair in TRAINING_PAIRS:
        vanna_client.train(question=pair["question"], sql=pair["sql"])
    return len(TRAINING_PAIRS)
