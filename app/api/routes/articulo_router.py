from fastapi import APIRouter, UploadFile, Form, status
from typing import List, Dict
from app.schemas.base_schema import APIResponse
from app.services.articulo_service import analizar_csv_articles, analizar_articulos_relevancia, obtener_matriz, insertar_articulo_detalle, listar_articulos_service, actualizar_relevancia_service, listar_articulos_detallados_service

router = APIRouter(prefix="/articulo", tags=["Gestion Articulo"])



@router.get(path="/detalle/{id_proyecto}")
async def listar_articulos_detallados_relevantes(id_proyecto: int):
    try:
        articulos = await listar_articulos_detallados_service(id_proyecto)
        return APIResponse(
            success=True,
            message="Artículos relevantes con detalle obtenidos correctamente",
            data=articulos,
            meta=None,
            status_code=status.HTTP_200_OK
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
            message="Error interno al actualizar relevancia",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.put(path="/detalle/{id_articulo_detalle}")
async def actualizar_relevancia(id_articulo_detalle: int, data: dict):
    try:
        es_relevante = data.get("es_relevante")
        result = await actualizar_relevancia_service(id_articulo_detalle, es_relevante)

        return APIResponse(
            success=True,
            message="Relevancia actualizada correctamente",
            data=result,
            meta=None,
            status_code=status.HTTP_200_OK
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
            message="Error interno al actualizar relevancia",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get(path="/{id_proyecto}")
async def listar_articulos(id_proyecto: int):
    try:
        articulos = await listar_articulos_service(id_proyecto)
   
        return APIResponse(
            success=True,
            message="Articulos analizados correctamente",
            data=articulos,
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
            message="Error interno al listar los articulos",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.post(path="/CSV")
async def analizar_articulo_endpoint(
    file: UploadFile,
    area_general: str = Form(...),
    tema_especifico: str = Form(...),
    problema_investigacion: str = Form(...),
    metodologia_enfoque : str = Form(...),
    id_proyecto : int = Form(...)
):
    try:
        contenido = await file.read()
        articulos = await analizar_csv_articles(contenido)
        articulos_analizados = await analizar_articulos_relevancia(articulos, area_general, tema_especifico, problema_investigacion, metodologia_enfoque, id_proyecto)
   
        return APIResponse(
            success=True,
            message="Articulos analizados correctamente",
            data=None,
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
    
   
@router.post(path="/detalle")
async def insertar_articulo_detalle_endpoint(articulos: List[Dict]):
    try:
        articulo = await insertar_articulo_detalle(articulos)
   
        return APIResponse(
            success=True,
            message="Detalles de los articulos insertados correctamente",
            data=articulo,
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
            message="Error interno al insertar los articulos",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
   

@router.post(path="/brecha")
async def obtener_brecha(
    file: UploadFile,
    area_general: str = Form(...),
    tema_especifico: str = Form(...),
    problema_investigacion: str = Form(...),
    metodologia_enfoque : str = Form(...)
):
    try:
        articulo = await obtener_matriz(file.file, area_general, tema_especifico, problema_investigacion, metodologia_enfoque)
   
        return APIResponse(
            success=True,
            message="Articulos analizados correctamente",
            data=articulo,
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
   
   
   


