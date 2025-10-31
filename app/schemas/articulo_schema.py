from pydantic import BaseModel
from typing import Optional, List, Literal



class Articulo(BaseModel):
    doi: Optional[str] = None
    titulo: Optional[str] = None
    resumen: Optional[str] = None
    anio: Optional[int] = None
    autores: Optional[List[str]] = None
    acceso_abierto: Optional[bool] = None
    autor_palabras_clave: Optional[str] = None
    index_palabras_clave: Optional[str] = None
    es_relevante: Optional[bool] = None

class ArticuloRequest(BaseModel):
    lista_articulo:  Optional[List[Articulo]] = None


class ArticuloResponseAPI(BaseModel):
    es_relevante: bool
    explicacion: str


class ResumenEstudio(BaseModel):
    objetivo_estudio: str
    metodologia: str
    hallazgos: str


class Brecha(BaseModel):
  
    tipo: Literal["conceptual", "metodológica", "de datos", "de comprensión", "de intervención"]
    descripcion: str
    evidencia_textual: str

class AnalisisBrechas(BaseModel):

    tipo_brecha : str
    brecha_principal: str
    