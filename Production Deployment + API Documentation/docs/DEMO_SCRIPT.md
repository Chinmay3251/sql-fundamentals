# 3-minute demo script

**0:00–0:20 — Introduction**
- State the problem: convert a CSV into business insights and an executive-ready presentation.
- Show the project README and the deployed app URL (replace the placeholder after deployment).

**0:20–0:55 — Health and API**
- Open `/health` and show `{"status":"ok"}`.
- Open `/docs` and explain the `/analyze` and `/export-ppt` endpoints.

**0:55–1:35 — Upload CSV and EDA**
- Use `data/sample_sales.csv` with `POST /analyze`.
- Show the five insights, recommendations, and executive summary.
- If Groq is configured, mention that the summary uses Groq; otherwise clearly identify the local fallback.

**1:35–2:20 — PowerPoint export**
- Upload the same CSV to `POST /export-ppt` and download the PPTX.
- Open the file and show the title slide, five insight slides, and recommendation slide.

**2:20–2:45 — Production verification**
- Show the output of `python scripts_smoke_test.py https://YOUR-DEPLOYMENT-URL`.
- Do not claim zero errors unless the production checks actually passed.

**2:45–3:00 — Wrap-up**
- Summarize the stack and known limitations.
- Show the final PR URL and link the demo recording after uploading it.
