from pathlib import Path
import argparse, logging
import pandas as pd
import sweetviz as sv
ROOT=Path(__file__).resolve().parents[1]
logging.basicConfig(filename=ROOT/'logs'/'eda.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
def main():
    p=argparse.ArgumentParser(); p.add_argument('--csv',default=str(ROOT/'data'/'sample_retail_sales.csv')); p.add_argument('--output',default=str(ROOT/'reports'/'sweetviz_report.html')); a=p.parse_args()
    path,out=Path(a.csv),Path(a.output)
    if not path.exists(): raise FileNotFoundError(path)
    out.parent.mkdir(parents=True,exist_ok=True); df=pd.read_csv(path)
    if df.empty: raise ValueError('Dataset is empty')
    try:
        sv.analyze(df).show_html(filepath=str(out),open_browser=False)
        logging.info('Sweetviz report saved to %s',out); print(f'Report saved: {out}')
    except Exception:
        logging.exception('Sweetviz run failed'); raise
if __name__=='__main__': main()
