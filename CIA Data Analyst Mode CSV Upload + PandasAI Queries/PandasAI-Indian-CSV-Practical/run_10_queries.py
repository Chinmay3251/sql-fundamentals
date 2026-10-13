from pathlib import Path
import logging, pandas as pd
from src.pandasai_runner import load_data, create_agent, ask
ROOT=Path(__file__).resolve().parent
logging.basicConfig(filename=ROOT/"logs"/"pandasai_errors.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
questions=pd.read_csv(ROOT/"reports"/"query_catalog.csv")
df=load_data(ROOT/"data"/"indian_retail_sales.csv")
agent=create_agent(df)
results=[ask(agent,q) for q in questions["natural_language_question"]]
out=ROOT/"reports"/"pandasai_query_results.csv"
pd.DataFrame(results).to_csv(out,index=False)
print(pd.DataFrame(results).to_string(index=False)); print(f"Saved {out}")
