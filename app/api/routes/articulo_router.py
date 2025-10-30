from fastapi import APIRouter, UploadFile, Form, status
from app.schemas.articulo_schema import Articulo
from typing import List
from app.schemas.base_schema import APIResponse
from app.services.articulo_service import analizar_csv_articles, analizar_articulos_relevancia, obtener_matriz

router = APIRouter(prefix="/articulo", tags=["Gestion Articulo"])


@router.post(path="/CSV")
async def analizar_articulo(
    file: UploadFile,
    area_general: str = Form(...),
    tema_especifico: str = Form(...),
    problema_investigacion: str = Form(...),
    metodologia_enfoque : str = Form(...)
):
    try:
        contenido = await file.read()
        articulos = await analizar_csv_articles(contenido)
        articulos_analizados = await analizar_articulos_relevancia(articulos, area_general, tema_especifico, problema_investigacion, metodologia_enfoque)
   
        return APIResponse(
            success=True,
            message="Articulos analizados correctamente",
            data=articulos_analizados,
            meta=None,
            status_code=status.HTTP_201_CREATED
        )
    except ValueError as e:
        return APIResponse(
            success=False,
            message="Error de validación",
            errors=str(e),
            status_code=status.HTTP_400_BAD_REQUEST
        )

    except Exception as e:
        return APIResponse(
            success=False,
            message="Error interno al analizar los articulos",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
   


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
