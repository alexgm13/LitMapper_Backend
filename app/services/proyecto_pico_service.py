
from app.external.proyecto_pico import generar_terminos_busqueda_ia, generar_ecuacion_busqueda_ia
from typing import List, Dict
import asyncio



async def generar_terminos_para_todos_pico(pico_list: List[Dict]):
    
    if not pico_list:
        raise ValueError("La lista de elementos PICO está vacía")
    
    tasks = []

    for pico in pico_list:
        tarea =  generar_terminos_busqueda_ia(pico)
        tasks.append(tarea)
    resultados = await asyncio.gather(*tasks)

    if not resultados:
        raise ValueError("No se generaron resultados válidos")
    

    return resultados

async def generar_ecuacion_busqueda(data: List[Dict]):

    if not data:
        raise ValueError("La lista de terminos esta vacia")
    ecuacion = await generar_ecuacion_busqueda_ia(data)
    return ecuacion