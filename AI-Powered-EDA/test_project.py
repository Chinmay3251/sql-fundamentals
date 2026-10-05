"""Lightweight manual verification tests for the EDA project."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "indian_retail_100k.csv"
REPORTS = ROOT / "reports"
CHARTS = REPORTS / "charts"

def main():
    assert DATA.exists(), "Dataset file is missing."
    df = pd.read_csv(DATA)
    assert len(df) == 100_000, f"Expected 100,000 rows, got {len(df):,}."
    required = {"order_id", "order_date", "state", "product", "category",
                "quantity", "unit_price", "customer_rating", "total_sales"}
    assert required.issubset(df.columns), f"Missing columns: {required - set(df.columns)}"
    assert (df["quantity"] >= 0).all(), "Negative quantities found."
    assert (df["total_sales"] >= 0).all(), "Negative total_sales found."
    assert (REPORTS / "data_quality_report.md").exists(), "Data quality report missing."
    assert (REPORTS / "eda_summary.md").exists(), "EDA summary missing."
    assert (REPORTS / "business_insights.md").exists(), "Business insights report missing."
    expected_charts = [
        "sales_by_category.png", "top_states_by_sales.png",
        "monthly_sales_trend.png", "sales_distribution.png"
    ]
    for chart in expected_charts:
        assert (CHARTS / chart).exists(), f"Chart missing: {chart}"
    print("PASS: dataset, required columns, value checks, reports, and charts verified.")

if __name__ == "__main__":
    main()
