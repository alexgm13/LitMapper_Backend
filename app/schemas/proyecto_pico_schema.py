from pydantic import BaseModel 
from typing import List



    
class PicoInput(BaseModel):
    elemento_pico:str
    descripcion_elemento:str


class PicoOutput(BaseModel):
    descripcion_elemento: str
    elemento_pico: str
    terminos_de_busqueda: List[str]

