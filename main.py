from fastapi import FastAPI
from app.api import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings


app = FastAPI(
    title="GapScan Backend",
    description="API para el análisis de artículos científicos usando IA Generativa",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.URL_CORS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def status():
    return {
        "status": "OK",
        "message" : "GapScan is running"
    }
