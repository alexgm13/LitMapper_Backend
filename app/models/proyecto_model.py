from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Proyecto(BaseModel):
    id_proyecto: Optional[int]
    titulo: str
    descripcion: str
    estado: Optional[str] = None
    etapa_actual: Optional[int] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None
    id_user: Optional[int] = None
