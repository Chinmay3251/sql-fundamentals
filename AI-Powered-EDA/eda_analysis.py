"""Core exploratory data analysis for the Indian retail business dataset."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "C:\Users\\MSI\\Desktop\\Internship\\AI-Powered-EDA\\data\\indian_retail_100k.csv"
REPORTS = ROOT / "reports"
CHARTS = REPORTS / "charts"

def main():
    REPORTS.mkdir(exist_ok=True)
    CHARTS.mkdir(parents=True, exist_ok=True)
    if not DATA.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA}. Run create_100k.py first.")

    # Load the data and parse dates for time-based analysis.
    df = pd.read_csv(DATA, parse_dates=["order_date"])
    required = {"order_date", "state", "city", "product", "category",
                "quantity", "unit_price", "total_sales"}
    missing_columns = required - set(df.columns)
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing_columns)}")

    # Data quality summary.
    quality = [
        "# Data Quality Report",
        "",
        f"- **Rows:** {len(df):,}",
        f"- **Columns:** {len(df.columns)}",
        f"- **Duplicate rows:** {int(df.duplicated().sum()):,}",
        "",
        "## Column data types",
        "",
        df.dtypes.astype(str).rename("dtype").to_frame().to_markdown(),
        "",
        "## Missing values",
        "",
        df.isna().sum().rename("missing_count").to_frame().to_markdown(),
        "",
        "## Numeric summary",
        "",
        df.describe(include="number").round(2).to_markdown(),
    ]
    (REPORTS / "data_quality_report.md").write_text("\n".join(quality), encoding="utf-8")

    # Business summaries.
    total_sales = df["total_sales"].sum()
    avg_order_value = df["total_sales"].mean()
    category_sales = df.groupby("category", dropna=False)["total_sales"].sum().sort_values(ascending=False)
    state_sales = df.groupby("state", dropna=False)["total_sales"].sum().sort_values(ascending=False).head(10)
    product_sales = df.groupby("product", dropna=False).agg(
        total_sales=("total_sales", "sum"),
        quantity_sold=("quantity", "sum")
    ).sort_values("total_sales", ascending=False)

    summary = [
        "# EDA Summary",
        "",
        f"- **Total sales:** {total_sales:,.2f}",
        f"- **Average transaction sales:** {avg_order_value:,.2f}",
        f"- **Total quantity sold:** {df['quantity'].sum():,}",
        f"- **Unique products:** {df['product'].nunique()}",
        f"- **Unique states:** {df['state'].nunique()}",
        f"- **Date range:** {df['order_date'].min().date()} to {df['order_date'].max().date()}",
        "",
        "## Sales by category",
        "",
        category_sales.rename("total_sales").to_frame().round(2).to_markdown(),
        "",
        "## Top 10 states by sales",
        "",
        state_sales.rename("total_sales").to_frame().round(2).to_markdown(),
        "",
        "## Product performance",
        "",
        product_sales.round(2).to_markdown(),
    ]
    (REPORTS / "eda_summary.md").write_text("\n".join(summary), encoding="utf-8")

    # Generate charts and save them for the final report.
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    category_sales.sort_values().plot(kind="barh")
    plt.title("Total Sales by Category")
    plt.xlabel("Total Sales")
    plt.tight_layout()
    plt.savefig(CHARTS / "sales_by_category.png", dpi=150)
    plt.close()

    plt.figure(figsize=(10, 6))
    state_sales.sort_values().plot(kind="barh")
    plt.title("Top 10 States by Sales")
    plt.xlabel("Total Sales")
    plt.tight_layout()
    plt.savefig(CHARTS / "top_states_by_sales.png", dpi=150)
    plt.close()

    monthly = df.dropna(subset=["order_date"]).assign(
        month=lambda x: x["order_date"].dt.to_period("M").astype(str)
    ).groupby("month")["total_sales"].sum()
    plt.figure(figsize=(11, 5))
    monthly.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS / "monthly_sales_trend.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.hist(df["total_sales"].dropna(), bins=30, edgecolor="black")
    plt.title("Distribution of Transaction Sales")
    plt.tight_layout()
    plt.savefig(CHARTS / "sales_distribution.png", dpi=150)
    plt.close()

    print(f"EDA completed: {len(df):,} rows, {len(df.columns)} columns")
    print(f"Total sales: {total_sales:,.2f}")
    print(f"Reports saved in: {REPORTS}")
    print(f"Charts saved in: {CHARTS}")

if __name__ == "__main__":
    main()
