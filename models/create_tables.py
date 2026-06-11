from db import Base, engine

from models.produto import Produto
from models.estoque import Estoque
from models.historico_estoque import HistoricoEstoque

Base.metadata.create_all(engine)