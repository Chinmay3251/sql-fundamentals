# Vanna CIA SQL Analyst — Practical Task

Deliverables: Vanna setup, PostgreSQL connection, 5 Q&A training pairs, 10 natural-language query tests with manual SQL review, and `POST /cia/sql-analyst`.

## Important schema assumption
The five examples assume:
- `products(product_id, product_name, stock, price)`
- `orders(...)`
- `order_items(product_id, quantity, ...)`

Inspect your Retail database and update example SQL plus `ALLOWED_TABLES` if names differ.

## 1. Prerequisites
- PostgreSQL Retail database running
- Ollama for Windows: https://ollama.com/download/windows
- Python 3.9+
- Recommended: use a dedicated read-only PostgreSQL account

Install/pull model:
```powershell
ollama pull qwen2.5:1.5b
ollama list
```

## 2. Install project dependencies
Run from this folder:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Configure database
```powershell
Copy-Item .env.example .env
notepad .env
```
Set actual `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`. Do not commit `.env`. Adjust `ALLOWED_TABLES`.

Example SQL for a DBA to create a read-only user (change password and database; connect to the database before schema grants):
```sql
CREATE USER retail_readonly WITH PASSWORD 'replace_with_a_strong_password';
GRANT CONNECT ON DATABASE retail TO retail_readonly;
GRANT USAGE ON SCHEMA public TO retail_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO retail_readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO retail_readonly;
```

Inspect schema:
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_name;
SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_schema='public' ORDER BY table_name, ordinal_position;
```

## 4. Train five Q&A pairs
After updating examples to match schema:
```powershell
python -c "from vanna_service import train_examples; print(train_examples())"
```
Local ChromaDB vector data is stored in `.vanna_chroma`.

## 5. Run API
Ensure Ollama is running and model is available:
```powershell
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
Docs: http://127.0.0.1:8000/docs
Health:
```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

End-to-end test:
```powershell
$body = @{ question = "Which products are low in stock?" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/cia/sql-analyst -ContentType "application/json" -Body $body
```

## 6. Ten-query testing
Questions are in `Tests/test_sql_analyst.py`; review checklist is `docs/manual_sql_review.md`. Run:
```powershell
python -m pytest Tests -q
```
The automated tests check endpoint basics and SQL safety. They do not claim to execute all ten live queries. Submit the completed `manual_test_results.csv` after running each question through the API and manually verifying joins, filters, aggregation, columns, ordering, and row counts.

## Endpoint
`POST /cia/sql-analyst`
Request JSON: `{"question":"Which products are low in stock?"}`
Response JSON contains `question`, `sql`, `results`, `row_count`.

## Safety
SQL parser permits read-only SELECT-style queries only, rejects multiple statements/comments, checks table allowlist, sets PostgreSQL transactions read-only, applies 10-second statement timeout, and caps output at 500 rows. Do not expose this API publicly without authentication.
