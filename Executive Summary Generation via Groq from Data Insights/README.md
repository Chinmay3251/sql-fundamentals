# CIA Groq EDA Executive Summary + PPT Export

Standalone starter for the CIA practical tasks. The actual CIA repository was not provided, so adapt these routes/modules into your project before merging.

## Run on Windows PowerShell
```powershell
cd CIA_Groq_EDA_PPT_Export
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
# Add GROQ_API_KEY in .env, then:
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Endpoints
- `POST /api/analyze`: upload CSV, run Pandas EDA, return five insights.
- `POST /api/summary`: generate a <=200-word Groq executive summary from exactly five insights.
- `POST /api/export-ppt`: export title + five insight slides + recommendations.
- `POST /api/full-flow`: upload CSV → EDA → summary → PPT download.
- `GET /health`: health check.

If no Groq API key is configured, a labeled local fallback summary allows the flow to be tested without credentials. Tests mock the summary step and do not call Groq. Run `pytest -q`.

CSV size is limited to 10 MB and 100,000 rows. This is a starter, not integrated with your existing CIA repo. Add authentication, rate limits and appropriate data handling before production use.
