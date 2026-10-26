# W8D2 — Business Recommendations: AI Narrative from Analytics

Practical FastAPI starter for **CSV upload → EDA → executive summary → PowerPoint download**.

## Includes
- CSV upload and validation.
- Five deterministic profiling insights and practical recommendations.
- Groq Chat Completions integration; summary limited to 200 words.
- Local fallback summary when `GROQ_API_KEY` is not configured or the request fails.
- PowerPoint with exactly seven slides: title, five insight slides, one recommendation slide.
- Pytest tests and sample sales CSV.

## Setup — Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
$env:GROQ_API_KEY = "YOUR_GROQ_API_KEY"
$env:GROQ_MODEL = "llama-3.3-70b-versatile"
```
The API key is optional; without it the app uses the fallback summary. Do not commit API keys.

## Run
```powershell
uvicorn app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## Test the complete flow
1. `POST /analyze`: upload `data/sample_sales.csv`; inspect the five insights and summary.
2. `POST /export-ppt`: upload the same CSV and download the returned PPTX.
3. Confirm the PPTX has seven slides.

PowerShell examples (run from project root):
```powershell
curl.exe -X POST "http://127.0.0.1:8000/analyze" -F "file=@data/sample_sales.csv"
curl.exe -X POST "http://127.0.0.1:8000/export-ppt" -F "file=@data/sample_sales.csv" --output business_recommendations.pptx
pytest -q
```

## Endpoints
- `GET /health` — health check
- `POST /analyze` — EDA report, five insights, recommendations, executive summary
- `POST /export-ppt` — downloadable PowerPoint

## Git workflow
Replace `[name]` with your branch suffix. Run commands separately in PowerShell:
```powershell
git status
git checkout -b feat/w8d2-3m-[name]
git add .
git commit -m "feat: add W8D2 analytics narrative and PPT export"
git add .
git commit -m "test: add W8D2 analytics and presentation tests"
git push -u origin feat/w8d2-3m-[name]
```
If your team requires rebasing on upstream, first verify `git remote -v`, then run `git fetch upstream` and `git rebase upstream/main` as separate commands. Update the PR after pushing.

## Scope notes
The insights are generic profiling insights; tailor them to your business domain as needed. The app re-analyses the uploaded CSV per endpoint and does not persist it. Tests are included but need to be run locally to verify your environment.
