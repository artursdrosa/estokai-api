from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from db import Base, engine


class HistoricoEstoque(Base):
    __tablename__ = 'historico_estoque'

    id = Column(Integer, primary_key=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    venda = Column(Boolean, nullable=False)
    quantidade = Column(Integer, nullable=False)
    data = Column(String(255), nullable=False)

Base.metadata.create_all(engine)