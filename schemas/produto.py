from typing import Optional
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None


class ProdutoRead(ProdutoBase):
    id: int

    class Config:
        orm_mode = True
