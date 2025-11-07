from pydantic import BaseModel
from app.schemas.proyecto_tema_schema import Contexto
from app.schemas.articulo_schema import ArticuloDetalle
from typing import List, Dict


class SoTA(BaseModel):
    contexto:Contexto
    articulos:List[Dict] 