from sqlalchemy import Column, Integer, ForeignKey
from db import Base, engine

class Estoque(Base):
    __tablename__ = 'estoque'

    id_produto = Column(Integer, ForeignKey('produtos.id'), primary_key=True)
    quantidade = Column(Integer, nullable=False, default=0)

Base.metadata.create_all(engine)