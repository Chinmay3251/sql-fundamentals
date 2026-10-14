from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data'/'sample_retail_sales.csv')
print(f'Rows: {len(df)} | Columns: {len(df.columns)} | Total sales: ${df.Sales.sum():,.2f}')
print('Sales by region:'); print(df.groupby('Region').Sales.sum().sort_values(ascending=False).round(2))
print('Sales by category:'); print(df.groupby('Category').Sales.sum().sort_values(ascending=False).round(2))
print('Missing values:'); print(df.isna().sum()[df.isna().sum()>0])
df['Order_Date']=pd.to_datetime(df.Order_Date); m=df.assign(Month=df.Order_Date.dt.to_period('M')).groupby('Month').Sales.sum(); print(f'Peak sales month: {m.idxmax()} (${m.max():,.2f})')
