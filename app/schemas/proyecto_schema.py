from pydantic import BaseModel


class ProyectoInsertar(BaseModel):
    titulo: str
    descripcion: str
    id_usuario: int