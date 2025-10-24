from openai import AsyncOpenAI
from app.core.config import settings
from typing import Dict
from app.schemas.articulo_schema import ArticuloResponseAPI, ResumenEstudio, AnalisisBrechas

client = AsyncOpenAI(api_key=settings.OPEN_API_KEY)


async def analizar_relevancia_ia(articulo: Dict, area_general: str, tema_especifico: str, problema_investigacion: str, metodologia_enfoque: str):
    response = await client.responses.parse(
        model="gpt-4o-mini",
        prompt={
        "id": "pmpt_68f9aa116718819392fb28a8e837530b0b951877105ae7c8",
        "version": "1",
        "variables": {
        "area_general": area_general,
        "tema_especifico": tema_especifico,
        "problema_investigacion": problema_investigacion,
        "metodologia_enfoque": metodologia_enfoque,
        "titulo": articulo["titulo"],
        "resumen": articulo["resumen"],
        "autor_palabras_clave":articulo["autor_palabras_clave"],
        "index_palabras_clave": articulo["index_palabras_clave"]
            }
        },
        text_format=ArticuloResponseAPI
    )
    return response.output_parsed


async def identificar_brecha_ia(texto:str, area_general: str, tema_especifico: str, problema_investigacion :str, metodologia_enfoque :str):
   
    
    response = await client.responses.parse(
    model="gpt-4o",
    prompt={
        "id": "pmpt_68fba2af5f0c819385a674fa2085908b09b287161accfda6",
        "version": "5",
        "variables": {
        "area_general": area_general,
        "tema_especifico":  tema_especifico,
        "problema_investigacion":  problema_investigacion,
        "metodologia_enfoque":  metodologia_enfoque,
        "texto_pdf": texto
            }
        },
        text_format=AnalisisBrechas
    )
    return response.output_parsed

    

async def extraccion_cognitiva_ia(texto_pdf:str):


    response = await client.responses.parse(
    model="gpt-4o-mini",
    prompt={
        "id": "pmpt_68fbbc48315c819495b4ab25ecd53a14030467127ca259fe",
        "version": "4",
        "variables": {
        "texto_pdf": texto_pdf
        }
    },
    text_format=ResumenEstudio
    )
    return response.output_parsed
