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

class Brecha(BaseModel):
    tipo: Literal["Conceptual", "Metodológica", "De Datos", "De Comprensión", "De Intervención"]
    descripcion: str
    sustento: Optional[str] = None


class ArticuloDetalle(BaseModel):
    problema_investigacion: str
    objetivo_estudio: str
    fundamento_teorico: str
    enfoque_metodologico: str
    muestra_poblacion:str
    instrumentos_tecnicas:str
    principales_resultados: str
    brechas_identificada: Brecha
    aportaciones:str
    notas_relevancia_contexto:str


