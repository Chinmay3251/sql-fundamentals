from pathlib import Path
import pandas as pd
def test_dataset():
 df=pd.read_csv(Path(__file__).resolve().parents[1]/'data'/'sample_retail_sales.csv')
 assert len(df)==800
 assert {'Order_Date','Region','Category','Sales','Profit'}.issubset(df.columns)
 assert (df.Sales.dropna()>=0).all()
