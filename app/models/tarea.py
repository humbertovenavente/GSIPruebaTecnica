from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TareaSchema(BaseModel):
    id_tarea: str
    tarea: str
    description: str
    estado: str
    prioridad: Optional[str] = "Media"
    fecha_creacion: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None
