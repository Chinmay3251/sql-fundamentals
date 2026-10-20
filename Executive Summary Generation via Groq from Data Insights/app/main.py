import io
import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from .eda import analyze_csv
from .groq_summary import generate_summary
from .ppt_export import build_presentation
load_dotenv()
app=FastAPI(title="CIA EDA Executive Summary and PPT Export",version="1.0.0")
MAX_BYTES=10*1024*1024; MAX_ROWS=100_000
class SummaryRequest(BaseModel): insights:list[str]=Field(min_length=5,max_length=5)
class ExportRequest(BaseModel):
    title:str="EDA Executive Brief"
    insights:list[str]=Field(min_length=5,max_length=5)
    recommendations:list[str]=[]
    summary:str=""
def parse_csv(raw):
    if not raw: raise HTTPException(400,"CSV file is empty.")
    if len(raw)>MAX_BYTES: raise HTTPException(413,"CSV exceeds 10 MB limit.")
    try: df=pd.read_csv(io.BytesIO(raw))
    except Exception: raise HTTPException(400,"Could not parse CSV; check encoding and format.")
    if df.empty: raise HTTPException(400,"CSV contains no data rows.")
    if len(df)>MAX_ROWS: raise HTTPException(413,f"CSV exceeds {MAX_ROWS:,}-row limit.")
    if len(df.columns)>200: raise HTTPException(400,"CSV exceeds 200-column limit.")
    return df
def ppt_response(title,insights,summary):
    recs=["Validate missing values, duplicates, and metric definitions before acting.","Investigate the largest observed differences and verify potential drivers.","Segment key metrics by available categories to identify variation.","Assign owners and review selected KPIs regularly."]
    data=build_presentation(title,insights,recs,summary)
    return StreamingResponse(io.BytesIO(data),media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",headers={"Content-Disposition":'attachment; filename="cia_eda_executive_brief.pptx"'})
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/api/analyze")
async def analyze(file:UploadFile=File(...)):
    if not file.filename or not file.filename.lower().endswith(".csv"): raise HTTPException(400,"Please upload a .csv file.")
    try: return analyze_csv(parse_csv(await file.read()))
    except ValueError as e: raise HTTPException(400,str(e))
@app.post("/api/summary")
def summary(req:SummaryRequest):
    try: return generate_summary(req.insights)
    except ValueError as e: raise HTTPException(400,str(e))
    except Exception as e: raise HTTPException(502,f"Groq summary request failed: {type(e).__name__}")
@app.post("/api/export-ppt")
def export_ppt(req:ExportRequest):
    try: return ppt_response(req.title,req.insights,req.summary)
    except ValueError as e: raise HTTPException(400,str(e))
@app.post("/api/full-flow")
async def full_flow(file:UploadFile=File(...)):
    if not file.filename or not file.filename.lower().endswith(".csv"): raise HTTPException(400,"Please upload a .csv file.")
    eda=analyze_csv(parse_csv(await file.read()))
    try: ai=generate_summary(eda["insights"])
    except Exception as e: raise HTTPException(502,f"Summary generation failed: {type(e).__name__}")
    data=build_presentation("EDA Executive Brief",eda["insights"],["Validate data quality and business metric definitions.","Investigate material variations and verify potential drivers.","Segment key measures by category and monitor changes.","Assign owners and review KPIs regularly."],ai["summary"])
    return StreamingResponse(io.BytesIO(data),media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",headers={"Content-Disposition":'attachment; filename="cia_eda_executive_brief.pptx"'})
