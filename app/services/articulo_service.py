import pandas as pd
from typing import List, Dict
import io, asyncio
import re, unicodedata
import fitz
from app.external.articulo import analizar_relevancia_ia, identificar_brecha_ia, extraccion_cognitiva_ia
from app.repositories.articulo_repository import insertar_articulo, insertar_articulo_detalle_db


def to_str(v) -> str:
    if v is None or (isinstance(v, float) and pd.isna(v)) or pd.isna(v):
        return ""
    return str(v)


def normalize_headers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    columns : List[str] = []
    for c in df.columns:
        columns.append(c.strip().lower())
    df.columns = columns
    return df


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

async def analizar_articulos_relevancia(articulos: List[Dict], area_general: str, tema_especifico: str, problema_investigacion: str, metodologia_enfoque: str):
            
            sem = asyncio.Semaphore(4)
            tasks = []
            async def _worker(articulo: Dict) -> Dict:
                async with sem:

                    id_articulo = await insertar_articulo(articulo)
                    resultado_ia = await analizar_relevancia_ia( articulo,area_general,tema_especifico,problema_investigacion, metodologia_enfoque)
                    
                    articulo_actualizado = {
                    "id_articulo" : id_articulo,
                    **articulo,
                    "detalle": {
                        "es_relevante": resultado_ia.es_relevante,
                        "explicacion": resultado_ia.explicacion
                    } 
                    }
                    return articulo_actualizado
            
            for articulo in articulos:
                tarea = asyncio.create_task(_worker(articulo))
                tasks.append(tarea)

            resultados = await asyncio.gather(*tasks)
            return resultados


def extraer_texto_pdf(file) -> str:

       texto = ""
       if isinstance(file, str):
            pdf = fitz.open(file)
       else:
            pdf = fitz.open(stream=file.read(), filetype="pdf")

       with pdf as doc:
           texto = "\n".join(page.get_text("text") for page in doc)
       return texto.strip()



def normalizar_texto_general(texto: str) -> str:


    texto = re.sub(r'\r', '\n', texto)              
    texto = re.sub(r'\n{2,}', '\n', texto)           

    texto = re.sub(r'-\s*\n', '', texto)

    texto = unicodedata.normalize("NFKC", texto)
    texto = texto.encode('utf-8', 'ignore').decode('utf-8', 'ignore')


    texto = re.sub(r'\bpage\s*\d+\b', '', texto, flags=re.IGNORECASE)
    texto = re.sub(r'\b(fig\.?|table|tabla|figura)\s*\d+\b', '', texto, flags=re.IGNORECASE)


    texto = texto.lower()
    texto = re.sub(r'\s+', ' ', texto)

    return texto.strip()


async def obtener_matriz(file, area_general: str, tema_especifico: str, problema_investigacion :str, metodologia_enfoque :str):
    texto = extraer_texto_pdf(file)
    print(texto)
    texto_normalizado = normalizar_texto_general(texto)
    texto_analizado = await extraccion_cognitiva_ia(texto_normalizado)
    print(texto_analizado)
    brecha = await identificar_brecha_ia(texto_normalizado, area_general, tema_especifico, problema_investigacion, metodologia_enfoque)
    print(brecha)
    detalle = {
        "detalle" :{
            "objetivo_estudio" : texto_analizado.objetivo_estudio,
            "metodologia" :  texto_analizado.metodologia,
            "hallazgos" : texto_analizado.hallazgos,
        },
        "brecha":{
            "brecha_investigacion" : brecha.brecha_principal,
            "tipo_brecha": brecha.tipo_brecha
        }
    }
    print(detalle)

    return detalle


async def insertar_articulo_detalle(articulos : List[Dict]):
     
    lista_id = []
    for articulo in articulos:
        id_detalle = await insertar_articulo_detalle_db(articulo)
        lista_id.append(id_detalle)
        
    return lista_id

     

        




 
        

    
