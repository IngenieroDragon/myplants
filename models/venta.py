from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Venta(BaseModel):
    fecha: Optional[datetime] = Field(default=None)
    garrafones: int
    medios: int
    galones: int
    total: float

