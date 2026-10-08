# Apache Superset — Complete Practical Task

Data source: Sample - Superstore.csv (1,000 rows, 16 columns).

## Task 1 — Superset locally with Docker
1. Start Docker Desktop.
2. From this folder run:
   docker compose up -d
3. Open http://localhost:8088.
4. Log in with the credentials created by the compose setup.
5. Connect Superset to PostgreSQL and use the imported `retail_sales` table.

## Task 2 — Build exactly 5 charts
Create one dashboard named `Retail Sales Dashboard` with:
1. Metric: Total Sales
2. Bar: Sales by Category
3. Line: Monthly Sales Trend
4. Pie: Sales by Region
5. Table: Top 10 Products by Sales

The SQL for each chart is in dashboard_queries.sql.

Expected values from this CSV:
Total Sales: $1,519,381.31
Category: {'Technology': 542529.3099999999, 'Furniture': 508183.53, 'Office Supplies': 468668.47000000003}
Region: {'West': 415429.53, 'East': 389580.67, 'South': 360902.64, 'Central': 353468.47}
Top product: Office Bookcase ($96,612.84)

The file `retail_dashboard_export_preview.png` is a visual reference/export-style PNG of the completed five-chart dashboard. After building the dashboard in Superset, use Superset's dashboard screenshot/export feature to create the actual Superset PNG.

## Task 3 — Present, feedback, improvement
Present the dashboard to one colleague. Ask:
- Is the dashboard easy to understand?
- Which chart is most useful?
- What would you improve?

Record the colleague's real feedback in feedback.md, then make exactly one improvement.
Example improvement: make the Total Sales KPI more prominent and add a date filter.

IMPORTANT: The example feedback must be replaced with the actual colleague feedback before submission.

## Suggested Git commits
git add .
git commit -m "feat: build Superset retail dashboard"
git add .
git commit -m "feat: improve retail dashboard after feedback"

Then follow your internship's required upstream rebase/push process.
