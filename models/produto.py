from sqlalchemy import Column, Integer, String, Float, ForeignKey
from db import Base


class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=True)
    preco = Column(Float, nullable=False)
