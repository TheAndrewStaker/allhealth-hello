from fastapi import FastAPI, Query, status
from pydantic import BaseModel
from core.app.greet import make_greeting
from adapters.tasks.tasks import process_ingest
from adapters.tasks.celery_app import celery_app

app = FastAPI(title="all.health hello (FastAPI)")

class IngestRequest(BaseModel):
    source: str
    value: float
    idempotency_key: str | None = None

@app.post("/ingest", status_code=status.HTTP_202_ACCEPTED)
def ingest(request: IngestRequest):
    #TODO generate/validate idempotency_key and persist it
    async_result = process_ingest.delay(request.model_dump())
    return {"job_id": async_result.id}

@app.get("/jobs/{job_id}")
def job_status(job_id: str):
    result = celery_app.AsyncResult(job_id)
    return {
        "job_id": job_id,
        "state": result.state,
        "result": result.result if result.successful() else None,
    }

@app.get("/hello")
def hello(name: str | None = Query(default=None)) -> dict:
    greeting = make_greeting(name)
    return {"message": greeting.message}
