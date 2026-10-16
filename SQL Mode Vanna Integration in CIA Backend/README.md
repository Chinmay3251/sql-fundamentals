# Week 7 Day 4 — Vanna CIA SQL Analyst

A FastAPI starter that exposes `POST /cia/sql-analyst`, uses Vanna's SQL-generation interface, includes five example question/SQL training pairs, and defines ten natural-language test questions plus a manual SQL review checklist.

> **Important:** This is a reference starter, not a verified integration with your internship's private CIA application or database. Database schema, model/provider configuration, and Vanna APIs vary by project/version. Review `src/vanna_service.py` and configure the actual schema before use. Do not expose this endpoint publicly without authentication and additional controls.

## Included
- FastAPI endpoint: `POST /cia/sql-analyst`
- Vanna adapter with five training Q&A pairs (SQL examples)
- SQL safety checks that allow read-only SELECT/WITH statements and reject multiple statements / write keywords
- 10 query test cases in `docs/test_queries.md`
- Manual SQL verification checklist and schema setup notes
- Unit tests for SQL guardrails (no database or LLM required)

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```
Fill `.env` with the database connection and model settings supported by your installed Vanna provider. Keep credentials private.

## Configure database schema
The example assumes a retail schema with `products(product_id, product_name, stock, price)`, `orders(order_id, customer_id, order_date, total_amount)`, and `order_items(order_id, product_id, quantity, unit_price)`. Adapt the schema and training SQL to match the real CIA database. Never assume these columns exist without checking.

## Run
```powershell
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```
Open `http://127.0.0.1:8000/docs` for the Swagger UI.

Example request:
```powershell
$body = @{ question = 'Which products are low in stock?' } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:8000/cia/sql-analyst' -ContentType 'application/json' -Body $body
```
The endpoint returns generated SQL and an execution status. Database execution is intentionally disabled by default; enable it only after reviewing the SQL, confirming least-privilege credentials, and implementing the database adapter for your schema. The response will say `execution_enabled: false` by default.

## Verify
```powershell
pytest -q
```
The included unit tests cover SQL guardrails and do not claim the model/database integration works. After configuring Vanna and your database, run the ten questions in `docs/test_queries.md`, inspect every generated query, execute approved read-only queries against a safe test database, and record the actual results in `docs/manual_verification.md`.

## Suggested Git commits
Make two meaningful commits after changes and local checks:
```powershell
git add src tests requirements.txt .env.example
git commit -m "feat: add Vanna CIA SQL analyst endpoint"
git add README.md docs
 git commit -m "docs: add SQL analyst training and verification guide"
```
Do not create empty commits. Fetch/rebase only after checking that `upstream` points to the instructor repository.
