# CIA CSV Analyst Starter

Implements CSV upload parsed by Pandas, temporary in-memory dataset storage, a query endpoint returning an answer plus Plotly-compatible JSON, and Chart.js rendering. This is a standalone scaffold because the actual CIA repository was not provided; adapt routes/components to your repo before merging.

## Run (PowerShell)
`cd backend` then `py -m venv .venv`, ` .\.venv\Scripts\Activate.ps1`, `python -m pip install -r requirements.txt`, `uvicorn app.main:app --reload`. Open API docs at http://127.0.0.1:8000/docs.
In another terminal: `cd frontend`, `py -m http.server 5500`, then open http://127.0.0.1:5500.

## API
`POST /api/upload` multipart field `file`; `POST /api/query` JSON `{dataset_id, question}`; `DELETE /api/dataset/{dataset_id}`. Uploaded data stays in backend memory until restart. 10 MB and 100,000 row limits.

PandasAI is optional; deterministic safe fallback supports row count, sum/average/min/max and grouping. To enable PandasAI, install/configure a supported provider and set `CIA_ENABLE_PANDASAI=true`. Do not enable arbitrary code execution in production without isolation, auth, and review.