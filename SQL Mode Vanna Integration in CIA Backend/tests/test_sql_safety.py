import pytest
from src.sql_safety import validate_read_only_sql

def test_select_is_allowed():
    assert validate_read_only_sql("SELECT * FROM products;") == "SELECT * FROM products"

def test_with_query_is_allowed():
    assert validate_read_only_sql("WITH x AS (SELECT 1) SELECT * FROM x") == "WITH x AS (SELECT 1) SELECT * FROM x"

@pytest.mark.parametrize("sql", ["", "DROP TABLE products", "UPDATE products SET stock=0", "SELECT 1; SELECT 2", "DELETE FROM orders"])
def test_unsafe_or_empty_sql_rejected(sql):
    with pytest.raises(ValueError):
        validate_read_only_sql(sql)
