from pydantic import BaseModel
from datetime import date
from typing import Optional


class TemaRegistrar(BaseModel):
    area_general: str
    tema_especifico: str
    problema_investigacion: str
    metodologia_enfoque:str
    id_proyecto: int


class TemaListar(BaseModel):
    id_proyecto:  int
  

class Contexto(BaseModel):
    id_contexto: Optional[int] = None
    area_general: str
    tema_especifico: str
    problema_investigacion: str
    metodologia_enfoque:str