import psycopg
from app.core.config import settings

DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

async def obtener_conexion():
    return await psycopg.AsyncConnection.connect(DATABASE_URL)
