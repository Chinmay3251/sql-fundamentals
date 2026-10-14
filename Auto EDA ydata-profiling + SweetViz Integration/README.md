# Week 7 Day 1 — AutoViz and Sweetviz EDA

## Tasks
- Run AutoViz and export its HTML report.
- Identify three insights.
- Run Sweetviz and export its HTML report.
- Compare the tools in 100 words.
- Recommend a tool for business stakeholders.

## Important honesty note
The two `*_preview.html` files are offline previews generated from the included CSV, **not native AutoViz/Sweetviz exports**. Run the scripts below to generate real reports using the installed packages. AutoViz output naming/behavior can vary by version.

## Dataset
`data/sample_retail_sales.csv` contains 800 **synthetic** retail rows for practice, not real company data. You can supply another CSV with `--csv`.

## Setup in Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Generate reports
```powershell
python src/run_autoviz.py
python src/run_sweetviz.py
```
Sweetviz output is `reports/sweetviz_report.html`. AutoViz files should appear in `reports/`; inspect console output for your installed version.

For a different dataset:
```powershell
python src/run_autoviz.py --csv "C:\path\dataset.csv" --output reports
python src/run_sweetviz.py --csv "C:\path\dataset.csv" --output "reports\sweetviz_report.html"
```

## Print calculated insights
```powershell
python src/analyze_dataset.py
```

## Initial insights from included CSV
1. Highest-sales region: **West**, $109,480.50.
2. Highest-sales category: **Technology**, $253,733.54.
3. Missing values exist in Discount, Profit and Customer_ID; investigate their causes and treatment before business reporting.

See `reports/comparison_and_recommendation.md` for the 100-word comparison and recommendation. Validate insights against the native reports after running them.

## Suggested meaningful commits
```powershell
git add README.md requirements.txt src
git commit -m "feat: add AutoViz and Sweetviz EDA scripts"
git add data reports
git commit -m "docs: add EDA dataset reports and findings"
```
Review the generated reports before committing; don't make empty commits.
