"""
Create a 100,000-row dataset from the supplied 1,500-row Indian retail CSV.
This repeats source rows to make a larger practice dataset; it does not create
100,000 independently observed real-world transactions.
"""
from pathlib import Path
import math
import pandas as pd

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "data" / "indian_retail_sales_1500.csv"
OUTPUT = ROOT / "data" / "indian_retail_100k.csv"
TARGET_ROWS = 100_000

def main():
    if not SOURCE.exists():
        raise FileNotFoundError(
            f"Source CSV not found: {SOURCE}. Place indian_retail_sales_1500.csv in data/."
        )
    source = pd.read_csv(SOURCE)
    if source.empty:
        raise ValueError("Source CSV is empty.")
    repeats = math.ceil(TARGET_ROWS / len(source))
    result = pd.concat([source] * repeats, ignore_index=True).iloc[:TARGET_ROWS].copy()
    result["order_id"] = range(1, TARGET_ROWS + 1)
    result["order_date"] = pd.to_datetime(
        result["order_date"], errors="coerce"
    ).dt.strftime("%Y-%m-%d")
    result.to_csv(OUTPUT, index=False)
    print(f"Created {OUTPUT} with {len(result):,} rows and {len(result.columns)} columns.")

if __name__ == "__main__":
    main()
