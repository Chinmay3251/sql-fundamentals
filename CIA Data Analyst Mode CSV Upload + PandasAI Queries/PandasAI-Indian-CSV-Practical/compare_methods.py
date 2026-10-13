from pathlib import Path
import logging, pandas as pd
from src.pandasai_runner import load_data, create_agent, ask
from src.manual_analysis import answer_question
ROOT=Path(__file__).resolve().parent
logging.basicConfig(filename=ROOT/"logs"/"pandasai_errors.log",level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
df=load_data(ROOT/"data"/"indian_retail_sales.csv")
agent=create_agent(df)
qs={"Q01":"What is the total revenue in INR?","Q03":"Which city has the highest total revenue?","Q06":"What is the average order revenue?"}
rows=[]
for qid,q in qs.items():
    ai=ask(agent,q)
    rows.append({"question_id":qid,"question":q,"manual_pandas_answer":str(answer_question(df,qid)),"pandasai_answer":ai["answer"],"success":ai["ok"],"accuracy_assessment":"Review against manual answer" if ai["ok"] else "Not assessable: failed","error":ai["error"]})
pd.DataFrame(rows).to_csv(ROOT/"reports"/"comparison_results.csv",index=False)
print(pd.DataFrame(rows).to_string(index=False))
