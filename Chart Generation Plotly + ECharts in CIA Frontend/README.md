# W7D3 — CIA Chart Generation: Plotly + ECharts

Standalone reference implementation for the Week 7 Day 3 task. The screenshot describes chart generation but does not include your existing CIA frontend source, so this demo is not a direct edit of that private repository.

## Features
- KPI cards: total sales, orders, average order value
- Monthly sales line chart and sales-by-category bar chart
- Switch between Plotly.js and Apache ECharts
- Responsive layout, chart labels, error handling, and sample-data tests

## Run on Windows PowerShell
Requires Node.js 18+ and internet access for chart libraries loaded from CDN.
```powershell
npm install
npm test
npm run dev
```
Open the local URL shown by Vite. Switch the library selector between Plotly and ECharts, resize the browser, and inspect the console for errors.

## Dataset
`data/retail_kpis.json` and `src/data.js` contain synthetic demonstration data, not real company results.

## Integration into CIA Frontend
Inspect the actual CIA repo first; preserve its routing, component conventions, styling system, and approved dependency versions. Reuse these chart configurations in the existing components rather than replacing the application entry point.

## Suggested commits
```powershell
git add README.md package.json index.html src data tests
git commit -m "feat: add Plotly and ECharts CIA chart demo"
```
Make a second descriptive commit only after a separate meaningful change, such as adding a real project integration or expanding tests. Then fetch/rebase against the verified instructor upstream, push your branch, and update the PR. This ZIP cannot push code or update a PR for you.

## Verification limitations
Automated tests validate data and KPI calculations, not browser rendering. Browser verification still needs to be performed locally.
