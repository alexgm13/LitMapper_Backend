from typing import List, Dict
from app.external.estado_arte import generar_sota_ia
from app.helpers.estado_arte import medir_entropia_sota

async def generar_sota_service(articulos: List[Dict], area_general: str, tema_especifico: str, problema_investigacion: str, metodologia_enfoque: str):
    
    if not articulos:
        raise ValueError("La lista de artículos no puede estar vacía.")

    if not area_general or not area_general.strip():
        raise ValueError("El 'área general' no puede estar vacía.")
    
    if not tema_especifico or not tema_especifico.strip():
        raise ValueError("El 'tema específico' no puede estar vacío.")
    
    if not problema_investigacion or not problema_investigacion.strip():
        raise ValueError("El 'problema de investigación' no puede estar vacío.")

    if not metodologia_enfoque or not metodologia_enfoque.strip():
        raise ValueError("La 'metodología' no puede estar vacía.")
    
    sota = await generar_sota_ia(articulos,area_general,tema_especifico,problema_investigacion,metodologia_enfoque)
    entropia = medir_entropia_sota(sota)
    return {
        "sota" : sota,
        "entropia": entropia
    }
