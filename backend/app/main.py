from fastapi import FastAPI
from backend.app.api.health import router as health_router

app = FastAPI(
    title="Solace AI",
    description="AI wellness companion for reflection, journaling, and personal growth.",
    version="0.1.0"
)

app.include_router(health_router, prefix="/api")