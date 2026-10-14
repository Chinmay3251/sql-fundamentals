from pathlib import Path
import argparse, logging
import pandas as pd
from autoviz import AutoViz_Class
ROOT=Path(__file__).resolve().parents[1]
logging.basicConfig(filename=ROOT/'logs'/'eda.log',level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
def main():
    p=argparse.ArgumentParser(); p.add_argument('--csv',default=str(ROOT/'data'/'sample_retail_sales.csv')); p.add_argument('--output',default=str(ROOT/'reports')); a=p.parse_args()
    path=Path(a.csv); out=Path(a.output); out.mkdir(parents=True,exist_ok=True)
    if not path.exists(): raise FileNotFoundError(path)
    df=pd.read_csv(path)
    if df.empty: raise ValueError('Dataset is empty')
    try:
        av=AutoViz_Class()
        av.AutoViz(filename=str(path),sep=',',depVar='',dfte=df,header=0,verbose=1,lowess=False,chart_format='html',max_rows_analyzed=150000,max_cols_analyzed=30,save_plot_dir=str(out))
        logging.info('AutoViz run completed; inspect output directory %s',out)
        print(f'AutoViz finished. Inspect {out} for generated HTML output; output filenames depend on package version.')
    except Exception:
        logging.exception('AutoViz run failed'); raise
if __name__=='__main__': main()
