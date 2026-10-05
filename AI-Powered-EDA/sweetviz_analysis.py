"""Generate an optional interactive Sweetviz HTML EDA report."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "indian_retail_100k.csv"
OUTPUT = ROOT / "reports" / "sweetviz_report.html"

def main():
    if not DATA.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA}")
    try:
        import sweetviz as sv
    except ImportError as exc:
        raise SystemExit("Sweetviz is not installed. Run: python -m pip install sweetviz") from exc

    df = pd.read_csv(DATA)
    report = sv.analyze(df)
    report.show_html(filepath=str(OUTPUT), open_browser=False)
    print(f"Sweetviz report saved to: {OUTPUT}")

if __name__ == "__main__":
    main()
