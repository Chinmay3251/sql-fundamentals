import logging, os
import pandas as pd
logger=logging.getLogger("pandasai_practical")

def load_data(path):
    df=pd.read_csv(path)
    df["order_date"]=pd.to_datetime(df["order_date"], errors="coerce")
    for col in ["quantity","unit_price_inr","discount_pct","revenue_inr"]:
        df[col]=pd.to_numeric(df[col], errors="coerce")
    return df

def create_agent(df):
    from pandasai import Agent
    from pandasai_litellm.openai import OpenAI
    if os.getenv("PANDASAI_MODEL","openai").lower() != "openai":
        raise ValueError("This starter is configured for the OpenAI provider.")
    llm=OpenAI(api_token=os.getenv("OPENAI_API_KEY"))
    return Agent(df, config={"llm":llm,"verbose":False,"save_logs":False})

def ask(agent, question):
    try:
        answer=agent.chat(question)
        if answer is None: raise ValueError("PandasAI returned an empty answer")
        logger.info("query_success question=%r",question)
        return {"ok":True,"question":question,"answer":str(answer),"error":""}
    except Exception as exc:
        logger.exception("query_failed question=%r",question)
        return {"ok":False,"question":question,"answer":"","error":f"{type(exc).__name__}: {exc}"}
