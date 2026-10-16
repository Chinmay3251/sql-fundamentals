"""CIA SQL analyst API. Database execution is disabled by default."""
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.sql_safety import validate_read_only_sql
from src.vanna_service import generator

app = FastAPI(title="CIA SQL Analyst", version="0.1.0")

class AnalystRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000, description="Question in natural language")

class AnalystResponse(BaseModel):
    question: str
    sql: str | None
    execution_enabled: bool
    status: str
    message: str

@app.get("/health")
def health():
    return {"status": "ok", "execution_enabled": os.getenv("ENABLE_SQL_EXECUTION", "false").lower() == "true"}

@app.post("/cia/sql-analyst", response_model=AnalystResponse)
def sql_analyst(payload: AnalystRequest):
    """Generate and safety-check SQL; do not execute it automatically."""
    try:
        generated = generator.generate_sql(payload.question)
        safe_sql = validate_read_only_sql(generated)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=f"Generated SQL rejected: {exc}") from exc
    except Exception as exc:
        # Avoid returning sensitive provider/DB details to callers.
        raise HTTPException(status_code=502, detail="SQL generation failed. Check server logs.") from exc

    # Intentional safety boundary: generated SQL is returned for manual review only.
    # Add execution only after implementing a read-only DB adapter and authorization.
    return AnalystResponse(
        question=payload.question,
        sql=safe_sql,
        execution_enabled=False,
        status="generated_needs_review",
        message="Review SQL against the real schema before executing it. Database execution is disabled.",
    )
