import pandas as pd
from typing import List, Dict
import io, asyncio
from fastapi.concurrency import run_in_threadpool
from app.helpers.articulo import extraer_texto_pdf, normalizar_texto_general, normalize_headers, to_str, calcular_taf, calcular_ici
from app.external.articulo import analizar_relevancia_ia, extraccion_cognitiva_ia
from app.repositories.articulo_repository import insertar_articulo, insertar_articulo_detalle_db, listar_articulos_db, articulo_articulo_relevancia_db, listar_articulos_detallados_db

async def listar_articulos_service(id_proyecto:int):
    articulos = await listar_articulos_db(id_proyecto)
    return articulos



async def listar_articulos_detallados_service(id_proyecto: int):
    return await listar_articulos_detallados_db(id_proyecto)


async def actualizar_relevancia_service(id_articulo_detalle: int, es_relevante: bool):
        
        actualizado = await articulo_articulo_relevancia_db(id_articulo_detalle, es_relevante)

        if not actualizado:
            raise ValueError("No se encontró el artículo detalle especificado")

        return {"id_articulo_detalle": id_articulo_detalle, "es_relevante": es_relevante}
    

async def analizar_csv_articles(data: bytes) -> List[Dict]:
    try:
        df = pd.read_csv(io.BytesIO(data), encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(io.BytesIO(data), encoding_errors="ignore")

    if df.empty:
        return []
    

    df = normalize_headers(df)
    results = []
    for i, row in df.iterrows():
        doi     = to_str(row.get("doi"))
        titulo = to_str(row.get("title"))
        resumen = to_str(row.get("abstract"))
        anio = to_str(row.get("year"))
        
        autor_palabras_clave = to_str(row.get("author keywords"))
        index_palabras_clave = to_str(row.get("index keywords"))
        results.append({
            "doi" : doi,
            "titulo" : titulo,
            "resumen": resumen,
            "anio": anio,
            "autor_palabras_clave":autor_palabras_clave,
            "index_palabras_clave": index_palabras_clave
        })

    return results

async def analizar_articulos_relevancia(articulos: List[Dict], area_general: str, tema_especifico: str, problema_investigacion: str, metodologia_enfoque: str, id_proyecto: int):
            
    sem = asyncio.Semaphore(4)
    tasks = []
    async def _worker(articulo: Dict) -> Dict:
        async with sem:

            resultado_ia = await analizar_relevancia_ia( articulo,area_general,tema_especifico,problema_investigacion, metodologia_enfoque)
            id_articulo = await insertar_articulo(articulo, resultado_ia.es_relevante, resultado_ia.explicacion, id_proyecto)
           

            return id_articulo
    
    for articulo in articulos:
        tarea = asyncio.create_task(_worker(articulo))
        tasks.append(tarea)

    resultados = await asyncio.gather(*tasks)
    return resultados





async def obtener_matriz(file, area_general: str, tema_especifico: str, problema_investigacion :str, metodologia_enfoque :str):
    texto = extraer_texto_pdf(file)
    texto_normalizado = normalizar_texto_general(texto)
    detalle = await extraccion_cognitiva_ia(area_general,tema_especifico, problema_investigacion, metodologia_enfoque, texto_normalizado)
    tfa =  calcular_taf(texto_normalizado, detalle.brechas_identificada.descripcion)
    ici = calcular_ici(texto_normalizado, detalle.brechas_identificada.descripcion)
    
    print(ici)
    print(tfa)

    return detalle


async def insertar_articulo_detalle(articulos : List[Dict]):
     
    lista_id = []
    for articulo in articulos:
        id_detalle = await insertar_articulo_detalle_db(articulo)
        lista_id.append(id_detalle)
        
    return lista_id

     

        




 
        

    
