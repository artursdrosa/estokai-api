from typing import Optional
from pydantic import BaseModel


class HistoricoEstoqueBase(BaseModel):
    produto_id: int
    venda: bool
    quantidade: int
    data: str


class HistoricoEstoqueCreate(HistoricoEstoqueBase):
    pass


class HistoricoEstoqueUpdate(BaseModel):
    produto_id: Optional[int] = None
    venda: Optional[bool] = None
    quantidade: Optional[int] = None
    data: Optional[str] = None


class HistoricoEstoqueRead(HistoricoEstoqueBase):
    id: int

    class Config:
        orm_mode = True
