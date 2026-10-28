# W8D3 — Production Deployment & Final Handoff

CSV analytics service that creates five EDA insights, an executive summary, and a seven-slide PowerPoint report.

## Features
- CSV upload with basic validation.
- Five data-derived profiling insights and business recommendations.
- Groq executive summary (maximum 200 words) when `GROQ_API_KEY` is configured; deterministic fallback otherwise.
- PowerPoint export: title slide, five insight slides, and recommendations slide.
- Health endpoint and production smoke-test script.

## Tech stack
Python 3.11, FastAPI, Pandas, Groq API, Requests, python-pptx, Uvicorn, Docker, Render or Railway, pytest, Git, GitHub.

## Local setup
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:GROQ_API_KEY = "YOUR_GROQ_API_KEY"
uvicorn app.main:app --reload
```
The Groq key is optional. Never commit API keys. Without it, the app uses a fallback summary.
Open `http://127.0.0.1:8000/docs`.

## Deploy on Render
1. Push this project to a GitHub repository.
2. In Render, create a new **Web Service** from the repository and choose Docker (the included `render.yaml` is a starting blueprint).
3. Add `GROQ_API_KEY` as a secret environment variable if using Groq. Set `GROQ_MODEL` if needed.
4. Deploy and wait for the service to become healthy.
5. Verify `https://YOUR-DEPLOYMENT-URL/health`, `/docs`, `/analyze`, and `/export-ppt`.

## Deploy on Railway
1. Create a Railway project from the GitHub repository.
2. Railway should detect the included `Dockerfile`; ensure the service uses it.
3. Add `GROQ_API_KEY` and optionally `GROQ_MODEL` in Variables.
4. Generate a public domain and wait for deployment to finish.
5. Verify the public URL with the checks below.

## Deployment URL
**Production URL:** `TODO — paste the real Render/Railway URL after deployment`

Do not leave the placeholder in the final PR. This project has not been deployed by the package generator; add the actual URL after you deploy it.

## Production smoke test
From the project root, with the deployed service reachable:
```powershell
python scripts_smoke_test.py https://YOUR-DEPLOYMENT-URL
```
The script checks `/`, `/health`, `/docs`, CSV analysis, and PPTX download. Run it against the real production URL and attach the output to the PR. A successful health check alone does not prove all features work.

## Tests
```powershell
pytest -q
```
Run locally before merging. Tests and production smoke checks must actually pass before reporting success.

## 3-minute demo video
Follow [`docs/DEMO_SCRIPT.md`](docs/DEMO_SCRIPT.md). Record the browser and presentation flow using your preferred screen recorder, upload the video to an approved shareable location, then add the actual demo URL to the final PR. **Demo URL:** `TODO — add recording link`.

## Known limitations
- Insights are generic dataset profiling, not domain-specific causal analysis.
- Uploaded CSVs are processed in memory for each request and are not persisted.
- Large CSVs may need request-size limits, background processing, and stronger resource controls before production use.
- Groq availability depends on a valid API key, model access, network access, and provider rate limits; the service falls back to a generic summary on API failure.
- No authentication or user-level access controls are included; do not expose sensitive datasets publicly without adding them.
- The included smoke-test script verifies core HTTP flows but is not a load, security, or full browser UI test.

## Final PR checklist
- [ ] Deploy and paste the real production URL above.
- [ ] Verify all features and review provider logs for HTTP 500 errors.
- [ ] Run `pytest -q` and `python scripts_smoke_test.py https://YOUR-DEPLOYMENT-URL`.
- [ ] Record and upload the 3-minute demo; paste the actual demo link.
- [ ] Include deployment details, test evidence, known limitations, and demo link in the PR description.
- [ ] Commit the README/deployment files and push the branch `feat/w8d3-3m-[name]`.
