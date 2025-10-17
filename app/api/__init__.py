from app.api.routes import all_routes
from fastapi import APIRouter

api_router = APIRouter()

for r in all_routes:
    api_router.include_router(r)