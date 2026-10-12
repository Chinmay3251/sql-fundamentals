
import os
import re

import sqlglot
from sqlglot import exp
from dotenv import load_dotenv

from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore


load_dotenv()


class RetailVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)


def quote_identifier(name):
    """Safely quote a PostgreSQL identifier."""
    return '"' + name.replace('"', '""') + '"'


def discover_schema(vn):
    """Read real table and column names from PostgreSQL."""
    query = """
        SELECT c.table_name, c.column_name, c.data_type
        FROM information_schema.columns AS c
        JOIN information_schema.tables AS t
          ON t.table_schema = c.table_schema
         AND t.table_name = c.table_name
        WHERE c.table_schema = 'public'
          AND t.table_type = 'BASE TABLE'
        ORDER BY c.table_name, c.ordinal_position
    """

    df = vn.run_sql(query)

    if df is None or df.empty:
        raise RuntimeError(
            "No public tables found. Check DB_NAME and permissions."
        )

    schema = {}

    for row in df.to_dict(orient="records"):
        table = row["table_name"]
        schema.setdefault(table, []).append(
            {
                "name": row["column_name"],
                "type": row["data_type"],
            }
        )

    return schema


def make_training_examples(schema):
    """
    Build exactly five examples using discovered identifiers.
    Examples are adapted to the actual Retail schema.
    """
    examples = []
    used_sql = set()

    def add(question, sql):
        if sql not in used_sql and len(examples) < 5:
            examples.append((question, sql))
            used_sql.add(sql)

    tables = {name.lower(): name for name in schema}

    # Example 1: products with low stock.
    product_table = tables.get("products")

    if product_table:
        cols = {
            c["name"].lower(): c["name"]
            for c in schema[product_table]
        }

        if "stock" in cols and "product_name" in cols:
            p = quote_identifier(product_table)
            add(
                "Which products are low in stock?",
                f"SELECT {quote_identifier(cols['product_name'])}, "
                f"{quote_identifier(cols['stock'])} "
                f"FROM {p} "
                f"WHERE {quote_identifier(cols['stock'])} < 10 "
                f"ORDER BY {quote_identifier(cols['stock'])} ASC"
            )

        if "price" in cols and "product_name" in cols:
            p = quote_identifier(product_table)
            add(
                "Which five products have the highest price?",
                f"SELECT {quote_identifier(cols['product_name'])}, "
                f"{quote_identifier(cols['price'])} "
                f"FROM {p} "
                f"ORDER BY {quote_identifier(cols['price'])} DESC "
                f"LIMIT 5"
            )

    # Example 2: most frequently ordered products.
    item_table = tables.get("order_items")

    if product_table and item_table:
        pcols = {
            c["name"].lower(): c["name"]
            for c in schema[product_table]
        }
        icols = {
            c["name"].lower(): c["name"]
            for c in schema[item_table]
        }

        if (
            "product_id" in pcols
            and "product_name" in pcols
            and "product_id" in icols
            and "quantity" in icols
        ):
            p = quote_identifier(product_table)
            i = quote_identifier(item_table)
            pid = quote_identifier(pcols["product_id"])
            name = quote_identifier(pcols["product_name"])
            qty = quote_identifier(icols["quantity"])
            item_pid = quote_identifier(icols["product_id"])

            add(
                "Which products have the highest units sold?",
                f"SELECT p.{name}, SUM(i.{qty}) AS units_sold "
                f"FROM {p} AS p "
                f"JOIN {i} AS i ON p.{pid} = i.{item_pid} "
                f"GROUP BY p.{pid}, p.{name} "
                f"ORDER BY units_sold DESC LIMIT 5"
            )

    # Example 3: count orders.
    orders_table = tables.get("orders")

    if orders_table:
        ocols = {
            c["name"].lower(): c["name"]
            for c in schema[orders_table]
        }

        if "order_id" in ocols:
            add(
                "How many orders are in the database?",
                f"SELECT COUNT(*) AS total_orders "
                f"FROM {quote_identifier(orders_table)}"
            )

    # Example 4: orders per customer.
    customers_table = tables.get("customers")

    if orders_table and customers_table:
        ocols = {
            c["name"].lower(): c["name"]
            for c in schema[orders_table]
        }
        ccols = {
            c["name"].lower(): c["name"]
            for c in schema[customers_table]
        }

        customer_name = next(
            (
                ccols[k]
                for k in ("customer_name", "name", "full_name")
                if k in ccols
            ),
            None,
        )

        if (
            "customer_id" in ocols
            and "customer_id" in ccols
            and customer_name
        ):
            o = quote_identifier(orders_table)
            c = quote_identifier(customers_table)
            oid = quote_identifier(ocols["customer_id"])
            cid = quote_identifier(ccols["customer_id"])
            cname = quote_identifier(customer_name)

            add(
                "How many orders has each customer placed?",
                f"SELECT c.{cname}, COUNT(o.{oid}) AS order_count "
                f"FROM {c} AS c "
                f"LEFT JOIN {o} AS o ON c.{cid} = o.{oid} "
                f"GROUP BY c.{cid}, c.{cname} "
                f"ORDER BY order_count DESC"
            )

    # Fill any missing examples with valid, schema-derived queries.
    # These fallback examples are intentionally generic.
    for table, columns in schema.items():
        qtable = quote_identifier(table)

        add(
            f"Show a sample of rows from the {table} table.",
            f"SELECT * FROM {qtable} LIMIT 10"
        )

        add(
            f"How many rows are in the {table} table?",
            f"SELECT COUNT(*) AS row_count FROM {qtable}"
        )

        if columns:
            col = quote_identifier(columns[0]["name"])
            add(
                f"Show the first 10 values of {columns[0]['name']} "
                f"from {table}.",
                f"SELECT {col} FROM {qtable} LIMIT 10"
            )

        if len(examples) == 5:
            break

    # Very small schemas may not provide five unique queries.
    # Use different LIMIT values to retain five distinct examples.
    if schema:
        table = quote_identifier(next(iter(schema)))

        for limit in (5, 15, 20, 25, 30):
            add(
                f"Show up to {limit} sample rows from the selected table.",
                f"SELECT * FROM {table} LIMIT {limit}"
            )

            if len(examples) == 5:
                break

    if len(examples) != 5:
        raise RuntimeError(
            "Could not construct five training examples."
        )

    return examples


def validate_read_only_sql(sql):
    """
    Accept one read-only SELECT statement.
    SQL generation does not execute the query.
    """
    if not isinstance(sql, str) or not sql.strip():
        return False, "The model returned empty SQL."

    # Remove common Markdown fences from model output.
    sql = re.sub(r"^\s*```(?:sql)?\s*", "", sql, flags=re.I)
    sql = re.sub(r"\s*```\s*$", "", sql)

    # Reject multiple statements.
    statements = sqlglot.parse(sql, read="postgres")

    if len(statements) != 1 or statements[0] is None:
        return False, "Only one SQL statement is allowed."

    tree = statements[0]

    # Only SELECT, UNION, INTERSECT or EXCEPT query roots are allowed.
    allowed_roots = (
        exp.Select,
        exp.Union,
        exp.Intersect,
        exp.Except,
    )

    if not isinstance(tree, allowed_roots):
        return False, "Only read-only SELECT queries are allowed."

    forbidden = (
        exp.Insert,
        exp.Update,
        exp.Delete,
        exp.Create,
        exp.Drop,
        exp.Alter,
        exp.Command,
    )

    if any(tree.find_all(kind) for kind in forbidden):
        return False, "The query contains a forbidden operation."

    return True, "Read-only query structure accepted."


def initialize_vanna():
    config = {
        "model": os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b"),
        "ollama_host": os.getenv(
            "OLLAMA_HOST", "http://localhost:11434"
        ),
    }

    vn = RetailVanna(config=config)

    vn.connect_to_postgres(
        host=os.getenv("DB_HOST", "localhost"),
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=int(os.getenv("DB_PORT", "5432")),
    )

    schema = discover_schema(vn)

    # Train on real table structure before question-SQL examples.
    for table, columns in schema.items():
        column_definitions = ", ".join(
            f"{quote_identifier(col['name'])} {col['type']}"
            for col in columns
        )

        ddl = (
            f"CREATE TABLE {quote_identifier(table)} "
            f"({column_definitions})"
        )

        vn.train(ddl=ddl)

    examples = make_training_examples(schema)

    for question, sql in examples:
        vn.train(question=question, sql=sql)

    print(f"Discovered {len(schema)} tables.")
    print(f"Trained {len(examples)} question-SQL examples.")

    for number, (question, sql) in enumerate(examples, start=1):
        print(f"\nTraining example {number}: {question}")
        print(sql)

    return vn


def generate_and_validate(vn, question):
    sql = vn.generate_sql(question=question)

    if not isinstance(sql, str):
        raise RuntimeError("Vanna did not return SQL text.")

    sql = re.sub(r"^\s*```(?:sql)?\s*", "", sql, flags=re.I)
    sql = re.sub(r"\s*```\s*$", "", sql).strip()

    valid, reason = validate_read_only_sql(sql)

    return {
        "question": question,
        "sql": sql,
        "valid": valid,
        "validation_message": reason,
    }
