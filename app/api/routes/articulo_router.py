from fastapi import APIRouter, UploadFile, Form
from app.schemas.articulo_schema import Articulo
from typing import List
from app.services.articulo_service import analizar_csv_articles, analizar_articulos_relevancia, obtener_matriz

router = APIRouter(prefix="/articulo", tags=["Gestion Articulo"])


@router.post(path="/analizar", response_model=List[Articulo])
async def analizar_articulo(
    file: UploadFile,
    area_general: str = Form(...),
    tema_especifico: str = Form(...),
    problema_investigacion: str = Form(...),
    metodologia_enfoque : str = Form(...)
):
    contenido = await file.read()
    articulos = await analizar_csv_articles(contenido)
    articulos_analizados = await analizar_articulos_relevancia(articulos, area_general, tema_especifico, problema_investigacion, metodologia_enfoque)
    return articulos_analizados


@router.post(path="/brecha")
async def obtener_brecha(
    file: UploadFile,
    area_general: str = Form(...),
    tema_especifico: str = Form(...),
    problema_investigacion: str = Form(...),
    metodologia_enfoque : str = Form(...),
    doi: str = Form (...)
):
   
   articulo = await obtener_matriz(file.file, area_general, tema_especifico, problema_investigacion, metodologia_enfoque, doi)

   return articulo
