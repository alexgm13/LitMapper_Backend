
from app.external.proyecto_pico import generar_terminos_busqueda_ia
from typing import List
import asyncio
from app.schemas.proyecto_pico_schema import PicoInput, PicoOutput


async def generar_terminos_para_todos_pico(pico_list: List[PicoInput]) -> List[PicoOutput]:
    tasks = []
    for pico in pico_list:
        tarea = asyncio.to_thread(generar_terminos_busqueda_ia, pico.model_dump())
        tasks.append(tarea)
    resultados = await asyncio.gather(*tasks)
    return resultados

