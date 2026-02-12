import logging

from adapters.tasks.celery_app import celery_app
from core.app.greet import make_greeting

logger = logging.getLogger(__name__)


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
def process_ingest(self, payload: dict) -> dict:
    source = payload.get("source") or "world"

    logger.info(
        "process_ingest started task_id=%s payload=%s",
        self.request.id,
        payload
    )

    greeting = make_greeting(source)

    response = {
        "task_id": self.request.id,
        "processed": True,
        "greeting": greeting.message,
        "received": payload
    }

    logger.info(
        "process_ingest finished task_id=%s response=%s",
        self.request.id,
        response
    )

    return response
