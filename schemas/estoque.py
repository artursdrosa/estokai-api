from typing import Optional
from pydantic import BaseModel


class EstoqueBase(BaseModel):
    id_produto: int
    quantidade: int = 0


class EstoqueCreate(EstoqueBase):
    pass


class EstoqueUpdate(BaseModel):
    quantidade: Optional[int] = None


class EstoqueRead(EstoqueBase):
    class Config:
        orm_mode = True
