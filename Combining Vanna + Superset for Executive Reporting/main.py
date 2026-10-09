from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from vanna_service import answer_question, ServiceError

app = FastAPI(title="CIA SQL Analyst", version="1.0.0")

class SQLAnalystRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=1000)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/cia/sql-analyst")
def sql_analyst(payload: SQLAnalystRequest):
    try:
        return answer_question(payload.question)
    except ServiceError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="SQL analyst failed; check server logs and configuration.") from exc
