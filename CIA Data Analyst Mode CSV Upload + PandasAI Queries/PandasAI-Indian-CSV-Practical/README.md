# PandasAI Practical — Indian Retail CSV

## Included
- 600-row Indian retail-style CSV (synthetic, clearly disclosed).
- 10 natural-language queries.
- PandasAI runner with error handling and logging.
- Manual Pandas reference answers and 3-question comparison script.
- Pytest checks, dataset profile, accuracy review template.

## Setup (Windows PowerShell)
Run each command separately:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```
Edit `.env` with a valid provider key. Never commit secrets. Provider integrations may change by PandasAI version; if the `pandasai_litellm.openai` import fails, follow the installed version's provider documentation and adapt `create_agent()` in `src/pandasai_runner.py`.

## Test
```powershell
python -m pytest -q
```

## Run 10 natural-language queries
```powershell
python run_10_queries.py
```
Outputs `reports/pandasai_query_results.csv`; logs errors to `logs/pandasai_errors.log`.

## Compare 3 questions with manual Pandas
```powershell
python compare_methods.py
```
Outputs `reports/comparison_results.csv`. Fill `reports/accuracy_review_template.md` from the actual run. AI results are not fabricated; a configured provider is required.

## Git
Use your task branch `feat/w6d5-3m-chinmay` if that matches your mentor's convention. Make at least two meaningful commits. Verify `git remote -v` and `git branch -r`; rebase only if `upstream/main` exists and is the correct instructor upstream. Then push and update your PR.
