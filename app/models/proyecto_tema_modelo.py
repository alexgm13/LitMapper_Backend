from pydantic import BaseModel
from typing import Optional

class DelimitacionTema(BaseModel):
    id_delimitacion: Optional[int] = None
    area_general: Optional[str]  = None
    tema_especifico: Optional[str] = None
    problema_investigacion: Optional[str] = None
    metodologia_enfoque: Optional[str] = None
    id_proyecto: Optional[int] = None