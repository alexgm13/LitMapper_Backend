from pydantic import BaseModel 
from typing import List



class ElementoPico(BaseModel):
    descripcion_elemento: str
    terminos_de_busqueda: List[str]

class PicoOutput(BaseModel):
    elemento_pico: ElementoPico
   

