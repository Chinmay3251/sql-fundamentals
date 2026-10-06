
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from vanna_service import initialize_vanna, generate_and_validate


vanna_instance = None
startup_error = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global vanna_instance, startup_error

    try:
        vanna_instance = initialize_vanna()
        startup_error = None
    except Exception as exc:
        startup_error = str(exc)
        print(f"Vanna startup failed: {startup_error}")

    yield


app = FastAPI(
    title="Retail Vanna SQL Analyst",
    description="Natural-language to read-only SQL generation",
    version="1.0.0",
    lifespan=lifespan,
)


class SQLAnalystRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Ask a question about the Retail database",
    )


@app.get("/")
def home():
    return {
        "service": "Retail Vanna SQL Analyst",
        "endpoint": "POST /cia/sql-analyst",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {
        "status": "ok" if vanna_instance is not None else "not_ready",
        "vanna_initialized": vanna_instance is not None,
        "startup_error": startup_error,
    }


@app.post("/cia/sql-analyst")
def sql_analyst(request: SQLAnalystRequest):
    if vanna_instance is None:
        raise HTTPException(
            status_code=503,
            detail=(
                "Vanna is not initialized. Check /health, "
                "the PostgreSQL connection, and Ollama."
            ),
        )

    try:
        result = generate_and_validate(
            vanna_instance,
            request.question,
        )
        return {
            "status": "success" if result["valid"] else "rejected",
            **result,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"SQL generation failed: {type(exc).__name__}",
        )
