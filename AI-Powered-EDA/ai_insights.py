"""
Create a business insights report from computed metrics.
If a local Ollama server is available, it can optionally draft the narrative.
All key figures are computed from the dataset before AI interpretation.
"""
from pathlib import Path
import json
import os
import pandas as pd
import requests

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "C:\\Users\\MSI\\Desktop\\Internship\\AI-Powered-EDA\\data\\indian_retail_100k.csv"
OUTPUT = ROOT / "reports" / "C:\\Users\\MSI\\Desktop\\Internship\\AI-Powered-EDA\\reports\\business_insights.md"

def build_metrics(df):
    category_sales = df.groupby("category")["total_sales"].sum().sort_values(ascending=False)
    state_sales = df.groupby("state")["total_sales"].sum().sort_values(ascending=False)
    product_sales = df.groupby("product")["total_sales"].sum().sort_values(ascending=False)
    monthly_sales = (
        df.assign(month=pd.to_datetime(df["order_date"], errors="coerce").dt.to_period("M").astype(str))
          .groupby("month")["total_sales"].sum().sort_values(ascending=False)
    )
    return {
        "row_count": int(len(df)),
        "total_sales": float(df["total_sales"].sum()),
        "average_transaction_sales": float(df["total_sales"].mean()),
        "total_quantity": int(df["quantity"].sum()),
        "category_sales": {str(k): float(v) for k, v in category_sales.items()},
        "top_5_states": {str(k): float(v) for k, v in state_sales.head(5).items()},
        "top_5_products": {str(k): float(v) for k, v in product_sales.head(5).items()},
        "highest_sales_month": str(monthly_sales.idxmax()) if len(monthly_sales) else "N/A",
        "lowest_sales_month": str(monthly_sales.idxmin()) if len(monthly_sales) else "N/A",
        "average_customer_rating": float(df["customer_rating"].mean()) if "customer_rating" in df else None,
    }

def ask_ollama(metrics):
    """Try local Ollama; return None if it is unavailable."""
    model = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
    prompt = (
        "You are a cautious business analyst. Interpret these computed retail metrics. "
        "Give 4-6 concise insights and practical recommendations. Do not invent figures, "
        "causal explanations, or facts not present in the metrics. Mention that the dataset "
        "was expanded by repeating a smaller source dataset if relevant. Metrics JSON:\n"
        + json.dumps(metrics, indent=2)
    )
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get("response", "").strip() or None
    except (requests.RequestException, ValueError):
        return None

def make_fallback(metrics):
    category = metrics["category_sales"]
    states = metrics["top_5_states"]
    products = metrics["top_5_products"]
    top_category = max(category, key=category.get) if category else "N/A"
    top_state = next(iter(states), "N/A")
    top_product = next(iter(products), "N/A")
    rating = metrics.get("average_customer_rating")
    text = [
        "## Data-backed observations",
        "",
        f"- The dataset contains **{metrics['row_count']:,} rows** and total recorded sales of **{metrics['total_sales']:,.2f}**.",
        f"- Average sales per row are **{metrics['average_transaction_sales']:,.2f}**.",
        f"- **{top_category}** is the highest-sales category in the supplied data.",
        f"- **{top_state}** is the highest-sales state among the grouped results.",
        f"- **{top_product}** is the highest-sales product in the grouped results.",
        f"- The highest-sales month is **{metrics['highest_sales_month']}** and the lowest-sales month is **{metrics['lowest_sales_month']}**.",
    ]
    if rating is not None:
        text.append(f"- Average customer rating is **{rating:.2f}**.")
    text += [
        "",
        "## Recommendations to investigate",
        "",
        "- Review inventory and supplier planning for the highest-sales products.",
        "- Compare state-level sales with customer counts, marketing spend, and delivery costs before reallocating budgets.",
        "- Investigate lower-sales categories and months to determine whether seasonality, stock availability, or product mix may explain the pattern.",
        "- Track customer ratings alongside sales to check whether customer experience differs by product, category, or state.",
        "",
        "## Interpretation note",
        "",
        "These recommendations are hypotheses for further investigation, not proof of cause and effect. Validate them with additional business data before making decisions.",
    ]
    return "\n".join(text)

def main():
    if not DATA.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA}")
    df = pd.read_csv(DATA)
    required = {"order_date", "state", "product", "category", "quantity", "total_sales"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    metrics = build_metrics(df)
    ai_text = ask_ollama(metrics)
    if ai_text:
        content = (
            "# AI-Powered Business Insights\n\n"
            "> AI-assisted interpretation of metrics calculated directly from the CSV. "
            "Review every statement before using it for business decisions.\n\n"
            + "## Computed metrics\n\n```json\n"
            + json.dumps(metrics, indent=2)
            + "\n```\n\n## AI interpretation\n\n"
            + ai_text
            + "\n\n## Validation reminder\n\nConfirm that each interpretation matches the computed metrics. "
              "The dataset used for this exercise may be synthetic or expanded from repeated source rows.\n"
        )
        mode = "Ollama-generated narrative"
    else:
        content = (
            "# AI-Powered Business Insights\n\n"
            "> The script computed the metrics from the CSV. Ollama was unavailable, so "
            "a transparent rule-based narrative was generated instead.\n\n"
            "## Computed metrics\n\n```json\n"
            + json.dumps(metrics, indent=2)
            + "\n```\n\n"
            + make_fallback(metrics)
            + "\n\n> Important: the source dataset is a practice dataset and the 100k-row version "
              "was expanded by repeating rows. Treat the findings as a demonstration, not as "
              "independent real-world market evidence.\n"
        )
        mode = "rule-based fallback (Ollama unavailable)"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Business insights saved to: {OUTPUT}")
    print(f"Report mode: {mode}")

if __name__ == "__main__":
    main()
