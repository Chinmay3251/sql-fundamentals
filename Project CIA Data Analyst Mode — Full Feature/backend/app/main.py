import io, uuid
import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from .analytics import answer_question
app=FastAPI(title="CIA CSV Analytics API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["http://127.0.0.1:5500","http://localhost:5500"],allow_methods=["GET","POST","DELETE"],allow_headers=["*"])
DATASETS={}; MAX_BYTES=10*1024*1024; MAX_ROWS=100000
class Query(BaseModel):
 dataset_id:str=Field(min_length=1,max_length=80)
 question:str=Field(min_length=3,max_length=500)
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/api/upload")
async def upload(file:UploadFile=File(...)):
 if not file.filename or not file.filename.lower().endswith(".csv"): raise HTTPException(400,"Please upload a .csv file.")
 raw=await file.read()
 if not raw: raise HTTPException(400,"Uploaded file is empty.")
 if len(raw)>MAX_BYTES: raise HTTPException(413,"CSV exceeds 10 MB limit.")
 try: df=pd.read_csv(io.BytesIO(raw))
 except Exception: raise HTTPException(400,"Could not parse CSV; check encoding and format.")
 if df.empty: raise HTTPException(400,"CSV contains no data rows.")
 if len(df)>MAX_ROWS: raise HTTPException(413,f"CSV exceeds {MAX_ROWS} row limit.")
 if len(df.columns)>200: raise HTTPException(400,"CSV must have at most 200 columns.")
 key=uuid.uuid4().hex; DATASETS[key]=df
 return {"dataset_id":key,"filename":file.filename,"rows":len(df),"columns":list(map(str,df.columns)),"preview":df.head().fillna("").astype(str).to_dict("records")}
@app.post("/api/query")
def query(p:Query):
 df=DATASETS.get(p.dataset_id)
 if df is None: raise HTTPException(404,"Dataset not found. Upload CSV again.")
 a=answer_question(df,p.question)
 return {"dataset_id":p.dataset_id,"question":p.question,"answer":a["answer"],"chart":a["chart"]}
@app.delete("/api/dataset/{dataset_id}")
def delete(dataset_id:str):
 if DATASETS.pop(dataset_id,None) is None: raise HTTPException(404,"Dataset not found.")
 return {"status":"deleted"}
