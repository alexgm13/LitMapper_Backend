from pydantic import BaseModel
from typing import Optional

class Proyecto(BaseModel):
    id_usuario: Optional[int] = None
    id_proyecto:Optional[int] = None
    titulo: str
    descripcion: str
    