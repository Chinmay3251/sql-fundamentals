import os
import re
from threading import Lock

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from sqlglot import parse_one, exp
from sqlglot.errors import ParseError
from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore

load_dotenv()
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "retail")
DB_USER = os.getenv("DB_USER", "retail_readonly")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")
ALLOWED_TABLES = {x.strip().lower() for x in os.getenv("ALLOWED_TABLES", "products,orders,order_items,customers").split(",") if x.strip()}

class ServiceError(RuntimeError):
    pass

class RetailVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self):
        ChromaDB_VectorStore.__init__(self, config={"path": "./.vanna_chroma"})
        Ollama.__init__(self, config={"model": OLLAMA_MODEL, "ollama_host": OLLAMA_HOST})

_vn = None
_lock = Lock()

def get_vanna():
    global _vn
    if _vn is None:
        with _lock:
            if _vn is None:
                _vn = RetailVanna()
    return _vn

def train_examples():
    """Train five sample Q&A pairs. Update SQL to match your actual schema first."""
    vn = get_vanna()
    examples = [
        ("Show all products", "SELECT product_id, product_name, stock FROM products ORDER BY product_name LIMIT 100"),
        ("Which products are low in stock?", "SELECT product_id, product_name, stock FROM products WHERE stock < 10 ORDER BY stock ASC"),
        ("Show the 10 most expensive products", "SELECT product_id, product_name, price FROM products ORDER BY price DESC LIMIT 10"),
        ("How many orders are there?", "SELECT COUNT(*) AS total_orders FROM orders"),
        ("What are the top 10 products by quantity sold?", "SELECT p.product_id, p.product_name, SUM(oi.quantity) AS total_quantity FROM products p JOIN order_items oi ON oi.product_id = p.product_id GROUP BY p.product_id, p.product_name ORDER BY total_quantity DESC LIMIT 10"),
    ]
    for question, sql in examples:
        vn.train(question=question, sql=sql)
    return {"trained_pairs": len(examples), "questions": [q for q, _ in examples]}

def validate_sql(sql):
    sql = sql.strip().rstrip(";").strip()
    if not sql or ";" in sql or "--" in sql or "/*" in sql:
        raise ServiceError("SQL rejected: empty SQL, multiple statements, or comments.")
    try:
        tree = parse_one(sql, read="postgres")
    except ParseError as exc:
        raise ServiceError(f"SQL parse error: {exc}") from exc
    if tree is None or not isinstance(tree, (exp.Select, exp.Union, exp.Intersect, exp.Except)):
        raise ServiceError("Only read-only SELECT queries are allowed.")
    if re.search(r"\b(insert|update|delete|drop|alter|create|truncate|grant|revoke|copy|call|execute)\b", sql, re.I):
        raise ServiceError("SQL rejected: write/administrative keyword detected.")
    names = {t.name.lower() for t in tree.find_all(exp.Table)}
    blocked = names - ALLOWED_TABLES
    if blocked:
        raise ServiceError("SQL references tables not in ALLOWED_TABLES: " + ", ".join(sorted(blocked)))
    return sql

def connect_db():
    if not DB_PASSWORD:
        raise ServiceError("DB_PASSWORD is not set. Copy .env.example to .env and configure it.")
    try:
        conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
            user=DB_USER, password=DB_PASSWORD, connect_timeout=5,
            options="-c default_transaction_read_only=on")
        conn.set_session(readonly=True, autocommit=False)
        return conn
    except Exception as exc:
        raise ServiceError(f"PostgreSQL connection failed; verify DB settings and server: {exc}") from exc

def answer_question(question):
    try:
        sql = get_vanna().generate_sql(question=question)
    except Exception as exc:
        raise ServiceError(f"Vanna/Ollama SQL generation failed: {exc}") from exc
    sql = validate_sql(sql)
    conn = connect_db()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SET LOCAL statement_timeout = '10s'")
            cur.execute(sql)
            rows = cur.fetchmany(500)
            return {"question": question, "sql": sql, "results": [dict(r) for r in rows], "row_count": len(rows)}
    finally:
        conn.rollback()
        conn.close()
