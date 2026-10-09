import pytest
from fastapi.testclient import TestClient
from main import app
from vanna_service import validate_sql, ServiceError

client = TestClient(app)

NATURAL_LANGUAGE_CASES = [
    "Show all products",
    "Which products are low in stock?",
    "Show the 10 most expensive products",
    "How many orders are there?",
    "What are the top 10 products by quantity sold?",
    "List products with stock below 5",
    "Show products sorted by name",
    "Count the number of products",
    "Show the 5 products with the lowest stock",
    "Show total quantity sold for each product",
]

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_short_question_rejected():
    assert client.post("/cia/sql-analyst", json={"question": "hi"}).status_code == 422

@pytest.mark.parametrize("sql", [
    "SELECT product_id FROM products",
    "SELECT COUNT(*) FROM orders",
    "SELECT p.product_name FROM products p JOIN order_items oi ON p.product_id = oi.product_id",
])
def test_select_allowed(sql):
    assert validate_sql(sql).upper().startswith("SELECT")

@pytest.mark.parametrize("sql", [
    "DELETE FROM products",
    "DROP TABLE products",
    "SELECT 1; DELETE FROM products",
])
def test_unsafe_sql_rejected(sql):
    with pytest.raises(ServiceError):
        validate_sql(sql)

def test_ten_manual_cases_listed():
    assert len(NATURAL_LANGUAGE_CASES) == 10
